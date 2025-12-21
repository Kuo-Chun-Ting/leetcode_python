class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        eamil_set = set()
        for email in emails:
            local_name = []
            domain_name = []
            char_valid = True

            for i in range(len(email)):
                if email[i] == ".":
                    continue

                if email[i] == "+":
                    char_valid = False
                    continue

                if email[i] == "@":
                    domain_name = email[i + 1 :]
                    break

                if char_valid:
                    local_name.append(email[i])

            final_email = f"{local_name}@{email[i:]}"
            eamil_set.add(final_email)

        return len(eamil_set)
