# File-Sharing-Man

<details>
<summary><h3><b>Deployment</b></h3></summary>

## 🚀 Heroku Deployment

<h4>Click the button below to deploy Indomie on Heroku!</h4>    
<a href="https://dashboard.heroku.com/new?template=https://github.com/IndomieGorengSatu/for-sell"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200"/></a>

</details>



<details>
<summary><h3><b>🔗 Extra Custom & List Vars</b></h3></summary>

### Variables

* `API_HASH` Dapatkan API HASH di web my.telegram.org.
* `API_ID` Dapatkan APP ID di web my.telegram.org
* `TG_BOT_TOKEN` Dapatkan dari t.me/BotFather
* `OWNER` Masukan Username Telegram untuk Owner BOT
* `CHANNEL_ID` Masukan ID Channel Untuk [Channel Database] contoh:- -100xxxxxxxx
* `ADMINS` Masukan User ID untuk mendapatkan hak Admin di BOT
* `START_MESSAGE` Opsional: Pesan /start memulai awalan ke bot, Gunakan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#start_message'>format</a> parsemode HTML 
* `FORCE_SUB_MESSAGE` Opsional: Pesan Paksa Subscribe bot, Gunakan Format parsemode HTML
* `FORCE_SUB_CHANNEL` Masukan ID dari Channel Untuk Wajib Subscribenya
* `FORCE_SUB_GROUP` Masukan ID dari Group Untuk Wajib Subscribenya

### Extra Variables

* `CUSTOM_CAPTION` letakkan teks teks Kustom Anda jika Anda ingin Mengatur Teks Kustom, Anda dapat menggunakan HTML dan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#custom_caption'>fillings</a> untuk pemformatan (hanya untuk dokumen)
* `DISABLE_CHANNEL_BUTTON` Masukan True untuk Nonaktifkan Tombol Berbagi Saluran, Default jika False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

</details>
