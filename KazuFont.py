

"""
◈ Perintah yang Tersedia -

• `{i}weeb <text>`
    turns text to 山乇乇乃 font

• `{i}tantext <text>`
    turns text to ᎿᎯᏁᎿᏋﾒᎿ font

• `{i}linetext <text>`
    turns text to 𝕃𝕀ℕ𝔼𝕋𝔼𝕏𝕋

• `{i}boxtext <text>`
    turns text to 🄱🄾🅇🅃🄴🅇🅃

• `{i}bubbletext <text>`
    turns text to ⒷⓊⒷⒷⓁⒺⓉⒺⓍⓉ

• `{i}cursive <text>`
    turns text to 𝓬𝓾𝓻𝓼𝓲𝓿𝓮 font

• `{i}greekify <text>`
    turns text to ϑгεεκιғψ font

• `{i}sorcify <text>`
    turns text to ֆօʀƈɛʀɛʀ font

• `{i}fraktify <text>`
    turns text to 𝖋𝖗𝖆𝖐𝖙𝖚𝖗𝖊 font

• `{i}rusify <text>`
    turns text to яц$їfч font

• `{i} font <font name>: <text>`\n Hasilkan font yang berbeda
     untuk teks | ketik {i} `font` Untuk Melihat Daftar Font
"""

from . import HNDLR, eod, kazu_cmd


normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
tantextfont = [
    "Ꭿ",
    "Ᏸ",
    "Ꮳ",
    "Ꮄ",
    "Ꮛ",
    "Ꮄ",
    "Ꮆ",
    "Ꮒ",
    "i",
    "Ꮰ",
    "Ꮶ",
    "l",
    "m",
    "Ꮑ",
    "Ꮻ",
    "Ꮅ",
    "Ꮔ",
    "ᖇ",
    "Ꭶ",
    "Ꮏ",
    "Ꮜ",
    "Ꮙ",
    "Ꮿ",
    "ﾒ",
    "Ꭹ",
    "Ꮓ",
]
linetextfont = [
    "𝔸",
    "𝔹",
    "ℂ",
    "𝔻",
    "𝔼",
    "𝔽",
    "𝔾",
    "ℍ",
    "𝕀",
    "𝕁",
    "𝕂",
    "𝕃",
    "𝕄",
    "ℕ",
    "𝕆",
    "ℙ",
    "ℚ",
    "ℝ",
    "𝕊",
    "𝕋",
    "𝕌",
    "𝕍",
    "𝕎",
    "𝕏",
    "𝕐",
    "ℤ",
]
boxtextfont = [
    "🄰",
    "🄱",
    "🄲",
    "🄳",
    "🄴",
    "🄵",
    "🄶",
    "🄷",
    "🄸",
    "🄹",
    "🄺",
    "🄻",
    "🄼",
    "🄽",
    "🄾",
    "🄿",
    "🅀",
    "🅁",
    "🅂",
    "🅃",
    "🅄",
    "🅅",
    "🅆",
    "🅇",
    "🅈",
    "🅉",
]
bubbletextfont = [
    "Ⓐ",
    "Ⓑ",
    "Ⓒ",
    "Ⓓ",
    "Ⓔ",
    "Ⓕ",
    "Ⓖ",
    "Ⓗ",
    "Ⓘ",
    "Ⓙ",
    "Ⓚ",
    "Ⓛ",
    "Ⓜ",
    "Ⓝ",
    "Ⓞ",
    "Ⓟ",
    "Ⓠ",
    "Ⓡ",
    "Ⓢ",
    "Ⓣ",
    "Ⓤ",
    "Ⓥ",
    "Ⓦ",
    "Ⓧ",
    "Ⓨ",
    "Ⓩ",
]
cursivefont = [
    "𝓪",
    "𝓫",
    "𝓬",
    "𝓭",
    "𝓮",
    "𝓯",
    "𝓰",
    "𝓱",
    "𝓲",
    "𝓳",
    "𝓴",
    "𝓵",
    "𝓶",
    "𝓷",
    "𝓸",
    "𝓹",
    "𝓺",
    "𝓻",
    "𝓼",
    "𝓽",
    "𝓾",
    "𝓿",
    "𝔀",
    "𝔁",
    "𝔂",
    "𝔃",
]
greekfont = [
    "λ",
    "ϐ",
    "ς",
    "d",
    "ε",
    "ғ",
    "ϑ",
    "н",
    "ι",
    "ϳ",
    "κ",
    "l",
    "ϻ",
    "π",
    "σ",
    "ρ",
    "φ",
    "г",
    "s",
    "τ",
    "υ",
    "v",
    "ш",
    "ϰ",
    "ψ",
    "z",
]
sorcererfont = [
    "ǟ",
    "ɮ",
    "ƈ",
    "ɖ",
    "ɛ",
    "ʄ",
    "ɢ",
    "ɦ",
    "ɨ",
    "ʝ",
    "ӄ",
    "ʟ",
    "ʍ",
    "ռ",
    "օ",
    "ք",
    "զ",
    "ʀ",
    "ֆ",
    "ȶ",
    "ʊ",
    "ʋ",
    "ա",
    "Ӽ",
    "ʏ",
    "ʐ",
]
frakturfont = [
    "𝖆",
    "𝖇",
    "𝖈",
    "𝖉",
    "𝖊",
    "𝖋",
    "𝖌",
    "𝖍",
    "𝖎",
    "𝖏",
    "𝖐",
    "𝖑",
    "𝖒",
    "𝖓",
    "𝖔",
    "𝖕",
    "𝖖",
    "𝖗",
    "𝖘",
    "𝖙",
    "𝖚",
    "𝖛",
    "𝖜",
    "𝖝",
    "𝖞",
    "𝖟",
]
rusifont = [
    "а",
    "б",
    "c",
    "д",
    "ё",
    "f",
    "g",
    "н",
    "ї",
    "j",
    "к",
    "г",
    "ѫ",
    "п",
    "ѳ",
    "p",
    "ф",
    "я",
    "$",
    "т",
    "ц",
    "ѵ",
    "щ",
    "ж",
    "ч",
    "з",
]

_default = string.ascii_letters
Fonts = {
    "small caps": "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "monospace": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉",
    "double stroke": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
    "script royal": "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵",
}


@kazu_cmd(
    pattern="font( (.*)|$)",
)
async def _(e):
    input = e.pattern_match.group(1).strip()
    reply = await e.get_reply_message()
    if not input:
        m = "**Available Fonts**\n\n"
        for x in Fonts.keys():
            m += f"• `{x}`\n"
        return await e.eor(m, time=5)
    if not reply:
        try:
            _ = input.split(":", maxsplit=1)
            font = _[0][:-1]
            text = _[1]
        except IndexError:
            return await eod(e, help)
    elif not input:
        return await eod(e, "`Give font dude :/`")
    else:
        font = input
        text = reply.message
    if font not in Fonts.keys():
        return await e.eor(f"`{font} not in font list`.", time=5)
    msg = gen_font(text, Fonts[font])
    await e.eor(msg)


def gen_font(text, new_font):
    new_font = " ".join(new_font).split()
    for q in text:
        if q in _default:
            new = new_font[_default.index(q)]
            text = text.replace(q, new)
    return text


@kazu_cmd(pattern="weeb ?(.*)")
async def weebify(kaz):
    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        await kaz.edit("What I am Supposed to Weebify? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await kaz.eor(string)


@kazu_cmd(pattern="tantext ?(.*)")
async def tantxt(kaz):
    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        await kaz.edit("What I am Supposed to tanify? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            tanycharacter = tantextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, tanycharacter)
    await kaz.eor(string)


@kazu_cmd(pattern="linetext ?(.*)")
async def linetxt(kaz):
    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        await kaz.edit("What I am Supposed to linefy? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            linecharacter = linetextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linecharacter)
    await kaz.edit(string)


@kazu_cmd(pattern="boxtext ?(.*)")
async def boxtxt(kaz):
    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        return await kaz.edit("What I am Supposed to boxify? Please Give Text Sir")
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boxcharacter = boxtextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boxcharacter)
    await kaz.eor(string)


@kazu_cmd(pattern="bubbletext ?(.*)")
async def bubbletxt(kaz):
    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        return await kaz.edit("What I am Supposed to bubblify? Please Give Text Sir")
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubbletextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)
    await kaz.eor(string)


@kazu_cmd(pattern="cursive ?(.*)")
async def cursive(kaz):
    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        return await kaz.edit(
            "What I am Supposed to write in cursive? Please Give Text Sir"
        )
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursivecharacter = cursivefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursivecharacter)
    await kaz.eor(string)


@kazu_cmd(pattern="greekify ?(.*)")
async def greektext(kaz):
    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        return await kaz.edit("What I am Supposed to greekify? Please Give Text Sir")
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            greekcharacter = greekfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, greekcharacter)
    await kaz.eor(string)


@kazu_cmd(pattern="sorcify ?(.*)")
async def sorcerertext(kaz):

    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        await kaz.edit("What I am Supposed to sorcify? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            sorcerercharacter = sorcererfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, sorcerercharacter)
    await kaz.eor(string)


@kazu_cmd(pattern="fraktify ?(.*)")
async def frakturtext(kaz):
    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        await kaz.edit("What I am Supposed to fraktify? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            frakturcharacter = frakturfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, frakturcharacter)
    await kaz.eor(string)


@kazu_cmd(pattern="rusify ?(.*)")
async def rusitext(kaz):
    args = kaz.pattern_match.group(1)
    if not args and kaz.is_reply:
        get = await kaz.get_reply_message()
        args = get.text
    if not args:
        return await kaz.edit("What I am Supposed to rusify? Please Give Text Sir")
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            rusicharacter = rusifont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, rusicharacter)
    await kaz.eor(string)
