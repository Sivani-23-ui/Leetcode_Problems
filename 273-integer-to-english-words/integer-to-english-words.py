class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six",
                "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]
        def small(n):
            if n < 20:
                return ones[n]
            if n < 100:
                return tens[n // 10] + (" " + ones[n % 10] if n % 10 else "")
            return ones[n // 100] + " Hundred" + (
                " " + small(n % 100) if n % 100 else ""
            )
        ans = []
        if num >= 1000000000:
            ans.append(small(num // 1000000000))
            ans.append("Billion")
            num %= 1000000000
        if num >= 1000000:
            ans.append(small(num // 1000000))
            ans.append("Million")
            num %= 1000000
        if num >= 1000:
            ans.append(small(num // 1000))
            ans.append("Thousand")
            num %= 1000
        if num > 0:
            ans.append(small(num))
        return " ".join(ans)