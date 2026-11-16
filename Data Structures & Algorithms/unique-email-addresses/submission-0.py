class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        ans = set()

        for s in emails:
            local_name, domain_name = s.split("@")
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            email = local_name + "@" + domain_name
            ans.add(email)

        return len(ans)

