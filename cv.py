# -*- coding: utf-8 -*-
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def print_banner():
    banner = """
    ============================================
    ||   JSON ↔ XML Converter Tool v1.0       ||
    ||       Created By Python 2.7            ||
    ============================================
    """
    print(banner)

def json_to_xml(json_obj, line_padding=""):
    result_list = []
    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json_to_xml(sub_elem, line_padding))
        return "".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append(
                "{}<{}>{}</{}>\n".format(
                    line_padding.strip(),
                    tag_name.strip(),
                    json_to_xml(sub_obj, "  " + line_padding),
                    tag_name.strip(),
                )
            )
        return "".join(result_list)
    return "{}{}".format(line_padding.strip(), str(json_obj).strip())


def format_xml(xml_string):
    try:
        dom = minidom.parseString(xml_string)
        pretty_xml_as_string = dom.toprettyxml(indent="  ")
        clean_lines = [line for line in pretty_xml_as_string.splitlines() if line.strip()]
        return "\n".join(clean_lines)
    except Exception as e:
        print("Error formatting XML: {}".format(e))
        return xml_string


def xml_to_json(xml_str):
    def parse_element(element):
        tag_dict = {}
        for child in element:
            tag_dict[child.tag] = parse_element(child)
        if element.text and element.text.strip():
            return element.text.strip()
        return tag_dict

    root = ET.fromstring(xml_str)
    return {root.tag: parse_element(root)}


def save_output(output_data, output_file):
    try:
        with open(output_file, "w") as file:
            file.write(output_data)
        print("Output berhasil disimpan di: {}".format(output_file))
    except Exception as e:
        print("Gagal menyimpan file: {}".format(e))


def main():
    print_banner()

    print("Pilih opsi:")
    print("1. Konversi JSON ke XML")
    print("2. Konversi XML ke JSON")
    choice = raw_input("Masukkan pilihan (1/2): ")

    if choice == "1":
        file_path = raw_input("Masukkan path file JSON: ")
        try:
            with open(file_path, "r") as json_file:
                json_data = json.load(json_file)
            xml_output = json_to_xml(json_data)
            formatted_xml = format_xml(xml_output)
            print("\nHasil XML:\n{}".format(formatted_xml))
            
            save_choice = raw_input("Simpan hasil ke file? (y/n): ")
            if save_choice.lower() == "y":
                output_file = raw_input("Masukkan nama file output (contoh: output.xml): ")
                save_output(formatted_xml, output_file)
        except Exception as e:
            print("Error: {}".format(e))

def main():
    print_banner()

    print("Pilih opsi:")
    print("1. Konversi JSON ke XML")
    print("2. Konversi XML ke JSON")
    choice = raw_input("Masukkan pilihan (1/2): ")

    if choice == "1":
        file_path = raw_input("Masukkan path file JSON: ")
        try:
            with open(file_path, "r") as json_file:
                json_data = json.load(json_file)
            xml_output = json_to_xml(json_data)
            formatted_xml = format_xml(xml_output)
            print("\nHasil XML:\n{}".format(formatted_xml))
            
            save_choice = raw_input("Simpan hasil ke file? (y/n): ")
            if save_choice.lower() == "y":
                output_file = raw_input("Masukkan nama file output (contoh: output.xml): ")
                save_output(formatted_xml, output_file)
        except Exception as e:
            print("Error: {}".format(e))

    elif choice == "2":
        file_path = raw_input("Masukkan path file XML: ")
        try:
            with open(file_path, "r") as xml_file:
                xml_data = xml_file.read()
            json_output = json.dumps(xml_to_json(xml_data), indent=4)
            print("\nHasil JSON:\n{}".format(json_output))
            
            save_choice = raw_input("Simpan hasil ke file? (y/n): ")
            if save_choice.lower() == "y":
                output_file = raw_input("Masukkan nama file output (contoh: output.json): ")
                save_output(json_output, output_file)
        except Exception as e:
            print("Error: {}".format(e))

    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
