import sys

def ask_question(question, correct_answer):
    answer = input(question + " ")
    return answer.strip().lower() == correct_answer.lower()

def main():
    questions = {
        "What is the default port for HTTP?": "80",
        "What does XSS stand for in web security?": "Cross-Site Scripting",
        "Who invented the World Wide Web?": "Tim Berners-Lee",
        "What does DNS stand for?": "Domain Name System",
        "What is the process of converting data into a coded format called?": "Encryption",
        "What protocol is commonly used for secure communication over the internet?": "HTTPS",
        "What does SQL stand for?": "Structured Query Language",
        "What is a common type of attack that involves injecting malicious code into a website?": "SQL Injection",
        "What type of malware encrypts files and demands payment for their release?": "Ransomware",
        "What is the practice of disguising communication to appear as though it is coming from a trusted source?": "Spoofing",
        "What is a file called that contains a digital certificate?": "Certificate",
        "What term describes the attempt to gain sensitive information by disguising as a trustworthy entity?": "Phishing",
        "What is a network device that filters and monitors incoming and outgoing network traffic?": "Firewall",
        "What type of attack involves overwhelming a system with traffic to disrupt service?": "DDoS",
        "What is the primary protocol used for sending email over the internet?": "SMTP",
        "What does VPN stand for?": "Virtual Private Network",
        "What is the name of the vulnerability that allows arbitrary code execution in software?": "Buffer Overflow",
        "What is the term for a software update that fixes bugs and vulnerabilities?": "Patch",
        "What does MFA stand for in cybersecurity?": "Multi-Factor Authentication",
        "What is a tool that scans a network for open ports and services?": "Nmap",
        "What is the name of the secure file transfer protocol that uses SSH?": "SFTP"
    }

    flag_parts = {
        0: "O",
        1: "S",
        2: "C",
        3: "T",
        4: "F",
        5: "{",
        6: "L",
        7: "3",
        8: "3",
        9: "t",
        10: "_",
        11: "K",
        12: "n",
        13: "0",
        14: "w",
        15: "l",
        16: "3",
        17: "D",
        18: "g",
        19: "3",
        20: "}"
    }

    revealed_flag = ["_"] * len(flag_parts)

    print("Answer the following cybersecurity questions to reveal the flag:")

    for index, (question, correct_answer) in enumerate(questions.items()):
        if ask_question(question, correct_answer):
            revealed_flag[index] = flag_parts[index]
            print(f"Correct! {''.join(revealed_flag)}")
        else:
            print("Incorrect. Start over again!")
            sys.exit(1)

    print(f"\nFinal flag: {''.join(revealed_flag)}")

if __name__ == "__main__":
    main()
