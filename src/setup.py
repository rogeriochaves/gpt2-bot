from gpt2_client import GPT2Client

# This could also be `345M` or `774M`
gpt2 = GPT2Client('117M', save_dir='models')
gpt2.load_model(force_download=False)
