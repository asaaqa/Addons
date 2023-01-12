
"""
◈ Perintah Tersedia

• `{i}border <reply to photo/sticker>`
    Untuk membuat batas di sekitar media itu ..
    Ex - `{i}border 12,22,23`
       - `{i}border 12,22,23 ; width (in number)`

• `{i}grey <reply to any media>`
    Untuk membuatnya hitam dan putih.

• `{i}color <reply to any Black nd White media>`
    Untuk membuatnya Berwarna-warni.

• `{i}toon <reply to any media>`
    Untuk membuatnya toon.

• `{i}danger <reply to any media>`
    Agar terlihat Bahaya.

• `{i}negative <reply to any media>`
    Untuk membuat citra negatif.

• `{i}blur <reply to any media>`
    Untuk membuatnya buram.

• `{i}quad <reply to any media>`
    membuat Vortex.

• `{i}mirror <reply to any media>`
    Untuk membuat gambar cermin.

• `{i}flip <reply to any media>`
    Untuk membuatnya terbalik.

• `{i}sketch <reply to any media>`
    Untuk menggambar sketsanya.

• `{i}blue <reply to any media>`
    hanya keren.

• `{i}csample <color name /color code>`
   example : `{i}csample red`
             `{i}csample #ffffff`

• `{i}pixelator <reply image>`
    Buat Gambar Piksel..
"""
import os

from . import LOGS, con

try:
    import cv2
except ImportError:
    LOGS.error(f"{__file__}: OpenCv not Installed.")

import numpy as np

try:
    from PIL import Image
except ImportError:
    Image = None
    LOGS.info(f"{__file__}: PIL  not Installed.")
from telegraph import upload_file as upf
from telethon.errors.rpcerrorlist import (
    ChatSendMediaForbiddenError,
    MessageDeleteForbiddenError,
)

from . import (
    Redis,
    async_searcher,
    download_file,
    get_string,
    requests,
    udB,
    kazu_cmd,
)


@kazu_cmd(pattern="color$")
async def _(event):
    reply = await event.get_reply_message()
    if not (reply and reply.media):
        return await event.eor("`Balas ke Gambar Hitam Putih`")
    xx = await event.eor("`Mewarnai gambar 🎨🖌️...`")
    image = await reply.download_media()
    img = cv2.VideoCapture(image)
    ret, frame = img.read()
    cv2.imwrite("kazu.jpg", frame)
    if udB.get_key("DEEP_API"):
        key = Redis("DEEP_API")
    else:
        key = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={"image": open("kazu.jpg", "rb")},
        headers={"api-key": key},
    )
    os.remove("kazu.jpg")
    os.remove(image)
    if "status" in r.json():
        return await event.edit(
            r.json()["status"] + "\nGet api nd set `{i}setdb DEEP_API key`"
        )
    r_json = r.json()["output_url"]
    await event.client.send_file(event.chat_id, r_json, reply_to=reply)
    await xx.delete()


@kazu_cmd(pattern="(grey|blur|negative|danger|mirror|quad|sketch|flip|toon)$")
async def kazu_tools(event):
    match = event.pattern_match.group(1)
    ureply = await event.get_reply_message()
    if not (ureply and (ureply.media)):
        await event.eor(get_string("cvt_3"))
        return
    kazu = await ureply.download_media()
    xx = await event.eor(get_string("com_1"))
    if kazu.endswith(".tgs"):
        xx = await xx.edit(get_string("sts_9"))
    file = await con.convert(kazu, convert_to="png", outname="kazu")
    kazu = cv2.imread(file)
    if match == "grey":
        kazu = cv2.cvtColor(kazu, cv2.COLOR_BGR2GRAY)
    elif match == "blur":
        kazu = cv2.GaussianBlur(kazu, (35, 35), 0)
    elif match == "negative":
        kazu = cv2.bitwise_not(kazu)
    elif match == "danger":
        dan = cv2.cvtColor(kazu, cv2.COLOR_BGR2RGB)
        kazu = cv2.cvtColor(dan, cv2.COLOR_HSV2BGR)
    elif match == "mirror":
        ish = cv2.flip(kazu, 1)
        kazu = cv2.hconcat([kazu, ish])
    elif match == "flip":
        trn = cv2.flip(kazu, 1)
        ish = cv2.rotate(trn, cv2.ROTATE_180)
        kazu = cv2.vconcat([kazu, ish])
    elif match == "quad":
        kazu = cv2.imread(file)
        roid = cv2.flip(kazu, 1)
        mici = cv2.hconcat([kazu, roid])
        fr = cv2.flip(mici, 1)
        trn = cv2.rotate(fr, cv2.ROTATE_180)
        kazu = cv2.vconcat([mici, trn])
    elif match == "sketch":
        gray_image = cv2.cvtColor(kazu, cv2.COLOR_BGR2GRAY)
        inverted_gray_image = 255 - gray_image
        blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
        inverted_blurred_img = 255 - blurred_img
        kazu = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)
    elif match == "toon":
        height, width, _ = kazu.shape
        samples = np.zeros([height * width, 3], dtype=np.float32)
        count = 0
        for x in range(height):
            for y in range(width):
                samples[count] = kazu[x][y]
                count += 1
        _, labels, centers = cv2.kmeans(
            samples,
            12,
            None,
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001),
            5,
            cv2.KMEANS_PP_CENTERS,
        )
        centers = np.uint8(centers)
        ish = centers[labels.flatten()]
        kazu = ish.reshape(kazu.shape)
    cv2.imwrite("kazu.jpg", kazu)
    await event.client.send_file(
        event.chat_id,
        "kazu.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("kazu.jpg")
    os.remove(file)


@kazu_cmd(pattern="csample (.*)")
async def sampl(kazu):
    if color := kazu.pattern_match.group(1).strip():
        img = Image.new("RGB", (200, 100), f"{color}")
        img.save("csample.png")
        try:
            try:
                await kazu.delete()
                await kazu.client.send_message(
                    kazu.chat_id, f"Contoh Warna untuk `{color}` !", file="csample.png"
                )
            except MessageDeleteForbiddenError:
                await kazu.reply(f"Contoh Warna untuk `{color}` !", file="csample.png")
        except ChatSendMediaForbiddenError:
            await kazu.eor("Hmm! Mengirim Media dinonaktifkan di sini!")

    else:
        await kazu.eor("Nama Warna/Kode Hex salah!")


@kazu_cmd(
    pattern="blue$",
)
async def kazu(event):
    ureply = await event.get_reply_message()
    xx = await event.eor("`...`")
    if not (ureply and (ureply.media)):
        await xx.edit(get_string("cvt_3"))
        return
    kazu = await ureply.download_media()
    if kazu.endswith(".tgs"):
        await xx.edit(get_string("sts_9"))
    file = await con.convert(kazu, convert_to="png", outname="kazu")
    got = upf(file)
    lnk = f"https://graph.org{got[0]}"
    r = await async_searcher(
        f"https://nekobot.xyz/api/imagegen?type=blurpify&image={lnk}", re_json=True
    )
    ms = r.get("message")
    if not r["success"]:
        return await xx.edit(ms)
    await download_file(ms, "kazu.png")
    img = Image.open("kazu.png").convert("RGB")
    img.save("kazu.webp", "webp")
    await event.client.send_file(
        event.chat_id,
        "kazu.webp",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("kazu.png")
    os.remove("kazu.webp")
    os.remove(kazu)


@kazu_cmd(pattern="border( (.*)|$)")
async def ok(event):
    hm = await event.get_reply_message()
    if not (hm and (hm.photo or hm.sticker)):
        return await event.eor("`Balas ke Stiker atau Foto..`")
    col = event.pattern_match.group(1).strip()
    wh = 20
    if not col:
        col = [255, 255, 255]
    else:
        try:
            if ";" in col:
                col_ = col.split(";", maxsplit=1)
                wh = int(col_[1])
                col = col_[0]
            col = [int(col) for col in col.split(",")[:2]]
        except ValueError:
            return await event.eor("`Bukan Masukan yang Valid...`")
    okla = await hm.download_media()
    img1 = cv2.imread(okla)
    constant = cv2.copyMakeBorder(img1, wh, wh, wh, wh, cv2.BORDER_CONSTANT, value=col)
    cv2.imwrite("output.png", constant)
    await event.client.send_file(event.chat.id, "output.png")
    os.remove("output.png")
    os.remove(okla)
    await event.delete()


@kazu_cmd(pattern="pixelator( (.*)|$)")
async def pixelator(event):
    reply_message = await event.get_reply_message()
    if not (reply_message and reply_message.photo):
        return await event.eor("`Membalas foto`")
    hw = 50
    try:
        hw = int(event.pattern_match.group(1).strip())
    except (ValueError, TypeError):
        pass
    msg = await event.eor(get_string("com_1"))
    image = await reply_message.download_media()
    input_ = cv2.imread(image)
    height, width = input_.shape[:2]
    w, h = (hw, hw)
    temp = cv2.resize(input_, (w, h), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("output.jpg", output)
    await msg.respond("• Pixelated by Kazu", file="output.jpg")
    await msg.delete()
    os.remove("output.jpg")
    os.remove(image)
