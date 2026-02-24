from supabase import create_client

# paste your credentials DIRECTLY
SUPABASE_URL = "https://txhvkhokeaganmazihbp.supabase.co"
SUPABASE_KEY = "sb_publishable_zhYFTzpwfBBizU39rcd7AA_WTrUOgaV"

print("Supabase URL:", SUPABASE_URL)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)