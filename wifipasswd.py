import subprocess
import re

def scan_string_for_pattern(input_string, pattern):
    # Split the input string into lines
    lines = input_string.split('\n')
    
    # Initialize a list to store matching lines
    matching_lines = []
    
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    # Iterate through each line and check for a match
    for line in lines:
        if regex.search(line):
            matching_lines.append(line)
    
    return matching_lines


def retrieve_wlan_profiles():
    try:
        # Run the netsh wlan show profiles command and capture the output
        output = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8")
        return output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

def extract_profile_names(output):
    # Define a regular expression pattern to match the "All User Profile" lines and capture the profile names
    pattern = re.compile(r"All User Profile\s*:\s*(.*)")
    profile_names = pattern.findall(output)
    return profile_names


if __name__ == "__main__":
    try:
        # Retrieve WLAN profiles' output
        wlan_profiles = retrieve_wlan_profiles()

        if wlan_profiles:
            # Extract profile names from the output
            profile_names = extract_profile_names(wlan_profiles)
            target_profiles = []
            
            if profile_names:
                print("WLAN Profile Names:")
                for profile_name in profile_names:
                    profile_name = profile_name.split("\r")[0]
                    output = subprocess.check_output(["netsh", "wlan", "show", "profiles", f"name={profile_name}", "key=clear"]).decode("utf-8")

                    # Specify the pattern to search for
                    search_pattern = r"Key Content"

                    # Scan the input string for lines containing the pattern
                    matching_lines = scan_string_for_pattern(output, search_pattern)
                        
                    # the matching lines
                    if matching_lines:
                        
                        for line in matching_lines:
                            line_list = line.split(":")
                            keys= line_list[1].split("\r")

                            target_profile = f"{profile_name} : {keys[0]}"
                            target_profiles.append(target_profile)

                            print(target_profile)
                    else:
                        print("No matches found.")
                    
            else:
                print("No WLAN profiles found.")
        else:
            print("Failed to retrieve WLAN profiles.")


        with open("wlan_passwords.txt", "w") as wlan_file:
            for profile in target_profiles:
                wlan_file.writelines(profile + "\n")

        print("\nwlan_password.txt created.\n")

    except:
        print("Something went wrong")
        print("\nwlan_password.txt NOT created.\n")