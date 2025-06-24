# Read a file and return its content
def read_file(filename):
    with open(filename, "r", encoding="utf8", errors='ignore') as file:
        content = file.read()
    return content

# Save a content to a file
def save_to_file(content, filename):
    with open(filename, "a", encoding="utf8", errors='ignore') as file:
        file.write(content)

# Load phrases from a dataset
def load_phrases(data_file_path):
    import pandas as pd
    data = pd.read_parquet(data_file_path)

    dataset_phrases = []
    for idx, row in data.iterrows():
        line_id = row['document name']
        tokens_content = ' '.join(row['tokens']).replace("'", "").replace(" .", ".").replace(" ,", ",").replace("( ", "(").replace(" )", ")")
        dataset_phrases.append(tokens_content)

    return dataset_phrases

# Parse the AI interaction to find the constraints
def parse_response_constraints (ai_reply):
    import re
    constraints = []
    str = "Final Formal Declarative Constraints"

    # Split the string after the last instace of "Final Formal Declarative Constraints:"
    index = ai_reply.rfind(str)
    if index == -1:
        return ["No constraints found in the AI reply."]
    else:
        # Split the string so that it contains only the constraints
        split_string = ai_reply[index + len(str):].strip()

        # Handle un-accepted symbols (everything that is not a letter or a number): /, ', ?, !, ...
        split_string = re.sub(r"[\/\'?!]", " ", split_string)

        # Define all available regex to find constraints
        # Unary constraints
        at_most_regex = re.compile(
            r"at-most\s*\(\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        existence_regex = re.compile(
            r"existence\s*\(\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        init_regex = re.compile(
            r"init\s*\(\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )

        # Binary constraints with exclusions
        response_regex = re.compile(
            r"(?<!not-)(?<!chain-)(?<!alternate-)response\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        precedence_regex = re.compile(
            r"(?<!not-)(?<!chain-)(?<!alternate-)precedence\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        succession_regex = re.compile(
            r"(?<!not-)(?<!chain-)(?<!alternate-)succession\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        choice_regex = re.compile(
            r"(?<!exclusive-)choice\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        chain_succession_regex = re.compile(
            r"(?<!not-)chain-succession\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        chain_response_regex = re.compile(
            r"(?<!not-)chain-response\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        chain_precedence_regex = re.compile(
            r"(?<!not-)chain-precedence\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        co_existence_regex = re.compile(
            r"(?<!not-)co-existence\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        exclusive_choice_regex = re.compile(
            r"(?<!not-)exclusive-choice\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        responded_existence_regex = re.compile(
            r"(?<!not-)responded-existence\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )

        # Binary constraints with no exclusions
        alternate_response_regex = re.compile(
            r"alternate-response\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        alternate_precedence_regex = re.compile(
            r"alternate-precedence\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        alternate_succession_regex = re.compile(
            r"alternate-succession\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )


        # Negative constraints
        not_response_regex = re.compile(
            r"not-response\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        not_precedence_regex = re.compile(
            r"not-precedence\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        not_chain_response_regex = re.compile(
            r"not-chain-response\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        not_chain_precedence_regex = re.compile(
            r"not-chain-precedence\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        not_chain_succession_regex = re.compile(
            r"not-chain-succession\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        not_co_existence_regex = re.compile(
            r"not-co-existence\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        not_exclusive_choice_regex = re.compile(
            r"not-exclusive-choice\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        not_responded_existence_regex = re.compile(
            r"not-responded-existence\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
            re.IGNORECASE
        )
        not_succession_regex = re.compile(
            r"not-succession\s*\(\s*([A-Za-z_ ]+)\s*,\s*([A-Za-z_ ]+)\s*\)", re.IGNORECASE)


        regexes = [at_most_regex, existence_regex, response_regex, precedence_regex, co_existence_regex, not_co_existence_regex, not_succession_regex, responded_existence_regex, alternate_succession_regex, init_regex, not_responded_existence_regex, not_response_regex, not_precedence_regex, not_chain_response_regex, not_chain_precedence_regex, succession_regex, choice_regex, exclusive_choice_regex, not_exclusive_choice_regex, not_chain_succession_regex, chain_succession_regex, chain_response_regex, chain_precedence_regex, alternate_response_regex, alternate_precedence_regex]
        constraints = ["at-most", "existence", "response", "precedence", "co-existence", "not-co-existence", "not-succession", "responded-existence", "alternate-succession", "Init", "not-responded-existence", "not-response", "not-precedence", "not-chain-response", "not-chain-precedence", "succession", "choice", "exclusive-choice", "not-exclusive-choice", "not-chain-succession", "chain-succession", "chain-response", "chain-precedence", "alternate-response", "alternate-precedence"]

        found_constraints = []
        for i in range(len(regexes)):
            regex = regexes[i]
            # Find all matches for the current regex in the split string
            matches = re.findall(regex, split_string)
            # if there are no matches for this regex, continue to the next one
            if not matches:
                print(f"\t\tNo matches found for {constraints[i]}")
                continue
            for match in matches:
                print(f"\t\tFound match for {constraints[i]}: {match}")
                # If the match is a tuple (for existence_pair), format it accordingly
                if isinstance(match, tuple):
                    formatted_match = constraints[i] + "(" + ", ".join(match) + ")"
                else:
                    formatted_match = constraints[i] + "(" + match + ")"
                
                found_constraints.append(formatted_match)
                formatted_match=""

        return found_constraints
    
# Finds the activities from the constraints
def parse_activities (constraints):
    import ast
    if type(constraints) is str:
        # If the input is a string, convert it to a list
        constraints = ast.literal_eval(constraints)
    activities = []
    for constraint in constraints:
        # Remove the constraint type and parentheses 
        # Be careful with the order of replacements, not-template should be done before template, symilarly co-template and template
        constraint  = constraint.replace("at-most(", "").replace("Init(", "").replace("not-responded-existence(", "").replace("responded-existence(", "").replace("not-co-existence(", "").replace("co-existence(", "").replace("existence(", "").replace("alternate-response(", "").replace("not-chain-response(", "").replace("chain-response(", "").replace("not-response(", "").replace("response(", "").replace("alternate-precedence(", "").replace("not-chain-precedence(", "").replace("chain-precedence(", "").replace("not-precedence(", "").replace("precedence(", "").replace("alternate-succession(", "").replace("not-chain-succession(", "").replace("chain-succession(", "").replace("not-succession(", "").replace("succession(", "").replace("not-exclusive-choice(", "").replace("exclusive-choice(", "").replace("choice(", "").replace(")", "").replace(" ", "")

        # Split process based on whether the constraint is unary or binary
        if "," in constraint:
            # Binary constraint
            parts = constraint.split(",")
            activities.append(parts[0])
            activities.append(parts[1])
        else:
            # Unary constraint
            activities.append(constraint)
    
    return list(set(activities))

# Parse the AI interaction to find the activities
def parse_response_activities (ai_reply):
    activities = []
    str = "Activities: "

    # Split the string after the last instace of "Final Formal Declarative Constraints:"
    index = ai_reply.rfind(str)
    if index == -1:
        return ["No activities found in the AI reply."]
    else:
        # Extract the line containing the activities
        lines = ai_reply[index:].split('\n')
        if lines:
            activity_line = lines[0]
            # Remove the "Activities: " part
            activity_line = activity_line.replace(str, "").strip()
            # Split by comma and strip whitespace
            activities = [act.strip() for act in activity_line.split(",") if act.strip()]    
    return activities

# Converts constraints and activities into a parsed string compaible with .decl syntax for model analysis
def parse_string_to_decl(constrains, activities):
    parsed_content = ""

    for activity in activities:
        parsed_content += f"activity {activity}\n"

    for constraint in constrains:
        constraint = constraint.replace("(", "[").replace(")", "]")
        # Split process based on whether the constraint is unary or binary
        if "," in constraint:
            # Binary constraint
            parsed_content += f"{constraint} | | |\n"
            
        else:
            # Unary constraint
            parsed_content += f"{constraint} | |\n"
            

    return parsed_content

# Builds a regex for binary constraints with optional exclusion prefixes
def build_binary_constraint(name, exclude_prefixes=None):
    import re
    if exclude_prefixes:
        lookbehinds = ''.join([f"(?<!{prefix}-)" for prefix in exclude_prefixes])
    else:
        lookbehinds = ''
    return f"""re.compile(
        r"{lookbehinds}{name}\s*\(\s*([\w\s\-]+?)\s*,\s*([\w\s\-]+?)\s*\)",
        re.IGNORECASE
    )"""

# Builds a regex for unary constraints with optional exclusion prefixes
def build_unary_constraint(name, exclude_prefixes=None):
    import re
    if exclude_prefixes:
        lookbehinds = ''.join([f"(?<!{prefix}-)" for prefix in exclude_prefixes])
    else:
        lookbehinds = ''

    return f"""re.compile(
        r"{lookbehinds}{name}\s*\(\s*([\w\s\-]+?)\s*\)",
        re.IGNORECASE
    )"""