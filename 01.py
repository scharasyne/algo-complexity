def check_if(text):
    if "if" in text:
        if "else" in text:
            return 2
        else: 
            return 1
    else:
        return 0

def check_for_if_nest(text):
    if check_if(text) == 2:
        print("nested if else inside!")
    elif check_if(text) == 1:
        print("only if inside")
    else:
        print("only_for")

def check_for(text):
    if "for" not in text:
        return 0
    else:
        check_for_if_nest(text)

def main():
    snippet = ""
    lines = int(input())
    while lines > 0:
        getInput = input()
        snippet += getInput
        lines -= 1
    
    check_for(snippet)
    # if check_for(snippet):

if __name__ == "__main__":
    main()

