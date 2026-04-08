from jiwer import wer, cer

def calculate_wer(reference, hypotesis):
    error_rate = wer(reference.lower(), hypotesis.lower())
    return error_rate * 100

def calculate_cer(reference, hypotesis):
    error_rate = cer(reference.lower(), hypotesis.lower())
    return error_rate * 100

if __name__ == "__main__":
    reference = "salom mening ismim oktam"
    hypotesis = "salom mening ismim uktam"

    print(f"Wer: {calculate_wer(reference, hypotesis):.2f}")
    print(f"CER: {calculate_cer(reference, hypotesis):.2f}")



