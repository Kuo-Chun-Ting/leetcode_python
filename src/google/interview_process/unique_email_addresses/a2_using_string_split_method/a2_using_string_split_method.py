class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        eamil_set = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")

            final_email = f"{local_name}@{domain_name}"
            eamil_set.add(final_email)

        return len(eamil_set)
