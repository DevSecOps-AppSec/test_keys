import xml.etree.ElementTree as ET

def parse_xml(data):
    try:
        # XXE vulnerability
        tree = ET.ElementTree(ET.fromstring(data))
        root = tree.getroot()
        return [elem.tag for elem in root]
    except ET.ParseError as e:
        return f"An error occurred during XML parsing: {e}"

def main():
    print("Welcome to the simple XML parser.")
    user_input = input("Enter your XML data: ")

    result = parse_xml(user_input)
    print(f"Parsed XML tags:\n{result}")

if __name__ == "__main__":
    main()
