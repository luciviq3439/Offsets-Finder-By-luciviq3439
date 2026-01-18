import os
import re
import tkinter as tk
from tkinter import filedialog

os.system("title MAGIC CHEATS OFFSETS FINDER")

# =========================
# TARGETS (boşluklar KORUNUR)
# =========================
TARGETS = [
    ("StaticClass", "0x5C"),
    ("MatchStatus", "0x3C"),
    ("LocalPlayer", "0x7C"),
    ("DictionaryEntities", "0x68"),

    None,

    ("Player_IsDead", "0x4C"),
    ("Player_Name", "protected string OIAJCBLDHKP;"),
    ("Player_ShadowBase", "public PlayerNetwork.HHCBNAPCKHF m_ShadowState;"),
    ("XPose", "0x78"),
    ("AvatarManager", "protected AvatarManager FOGJNGDMJKJ;"),
    ("Avatar", "0x94"),
    ("Avatar_IsVisible", "0x7C"),
    ("Avatar_Data", "0x10"),
    ("Avatar_Data_IsTeam", "0x51"),
    ("CurrentMatch", "0x50"),

    None,

    ("FollowCamera", "protected FollowCamera CHDOHNOEBML;"),
    ("Camera", "0x14"),
    ("AimRotation", "private Quaternion <KCFEHMAIINO>k__BackingField;"),
    ("MainCameraTransform", "public Transform MainCameraTransform;"),

    None,

    ("Weapon", "public GPBDEDFKJNA ActiveUISightingWeapon;"),
    ("WeaponData", "0x58"),
    ("WeaponRecoil", "0xC"),
    ("ViewMatrix", "0x98 + 0x24"),

    None,

    ("Silent1", "private bool <LPEIEILIKGC>k__BackingField;"),
    ("Silent2", "private MADMMIICBNN GEGFCFDGGGP;"),
    ("Silent3", "0x38"),
    ("Silent4", "0x2C"),

    None,

    ("HeadCollider", "protected Collider HECFNHJKOMN;"),

    None,

    ("PlayerAttributes", "protected PlayerAttributes JKPFFNEMJIF;"),
    ("NoReload", "0x91"),

    None,

    ("isBot", "public bool IsClientBot;"),

    None,

    ("Head", "protected ITransformNode OLCJOGDHJJJ;"),
    ("Root", "protected ITransformNode MPJBGDJJJMJ;"),
    ("LeftWrist", "protected ITransformNode GCMICMFEAKI;"),
    ("Spine", "protected ITransformNode HCLMADAFLPD;"),
    ("Hip", "protected ITransformNode CENAIGAFGAG;"),
    ("RightCalf", "protected ITransformNode JPBJIMCDBHN;"),
    ("LeftCalf", "protected ITransformNode BMGCHFGEDDA;"),
    ("RightFoot", "protected ITransformNode AGHJLIMNPJA;"),
    ("LeftFoot", "protected ITransformNode FDMBKCKMODA;"),
    ("RightWrist", "protected ITransformNode CKABHDJDMAP;"),
    ("LeftHand", "protected ITransformNode KOCDBPLKMBI;"),
    ("LeftShoulder", "protected ITransformNode LIBEIIIAGIK;"),
    ("RightShoulder", "protected ITransformNode HDEPJIBNIIK;"),
    ("RightWristJoint", "protected ITransformNode NJDDAPKPILB;"),
    ("LeftWristJoint", "protected ITransformNode JHIBMHEMJOL;"),
    ("LeftElbow", "protected ITransformNode JBACCHNMGNJ;"),
    ("RightElbow", "protected ITransformNode FGECMMJKFNC;"),
]

# =========================
def select_dump_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="dump.cs select",
        filetypes=[("C# Dump", "*.cs")]
    )

def extract_hex(line):
    match = re.search(r'0x[0-9A-Fa-f]+', line)
    return match.group(0) if match else None

def is_hex(value):
    return isinstance(value, str) and value.startswith("0x")

def search_strings(file_path, targets):
    results = {}

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    for item in targets:
        if item is None:
            continue

        name, key = item

        # Hex ise sabit
        if is_hex(key):
            results[name] = key
            continue

        # String ise dump içinde ara
        for line in lines:
            if key in line:
                offset = extract_hex(line)
                if offset:
                    results[name] = offset
                break

    return results

def print_simple(title, data, targets):
    print(f"\n====== {title} ======")
    for item in targets:
        if item is None:
            print()
            continue

        name, _ = item
        if name in data:
            print(f"{name} {data[name]}")
        else:
            print(f"{name} NOT FOUND")

# =========================
if __name__ == "__main__":
    dump_path = select_dump_file()
    if not dump_path:
        print("dump.cs not selected")
        exit()

    string_offsets = search_strings(dump_path, TARGETS)
    print_simple("OFFSETS", string_offsets, TARGETS)

    input("\nPress Enter For Close...")
