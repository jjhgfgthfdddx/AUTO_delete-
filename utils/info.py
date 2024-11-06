import os

API_ID       = int(os.environ.get("API_ID", "19071424"))
API_HASH     = os.environ.get("API_HASH", "c4b3e298cc50fd4cc563ae75ee882948")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6724470726:AAEqA0FQME2Bh7DVN2dJhpQdwOM3iMEA7l0")
SESSION      = os.environ.get("SESSION", "BQG1_SUAIzL4MN7ryZsmM3RF23ERZ5R3xxBnfU4lzQuih2ODJfFkCdQqOG5EOQVxou1dIIftnHdU0xQDl4bdCvs3mNSO3q5b3Z1T5N3_2SlpngGF-3ypEyJXI1ALI-JTsAF0p3y7qifi1maH6PzqHUda-wu0FsawdjLO3Xs1jjbApSpS620PelLgkO_iSxzAK4XhbYtNmn9fdcVqXp8MCvdBRtbDfoPCEt8hDmjyzjjqJXT6S10HtCe3v9ZLquaKx_MaFrk2Hlnta-rPVPnacrXirgj4H_qqgAq44wmtuUxC_Hk6UD6Wb3bCHNpp9OL8JvKX-AAoch8b7Sg9tc2_0XYGWrWCLQAAAAHFiGJyAA")
TIME         = int(os.environ.get("TIME", 1))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "")
PORT         = os.environ.get("PORT", "8080")
