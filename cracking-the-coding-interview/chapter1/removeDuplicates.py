class List(object):
    def __init__(self, value) -> None:
        self.next = None
        self.value = value

    @staticmethod
    def generate(ls):
        if not ls:
            return None

        curr = List(ls[0])
        head = curr
        for x in range(1, len(ls)):
            curr.next = List(ls[x])
            curr = curr.next

        return head
    
    def trace(self):
        curr = self
        while curr:
            print(curr.value)
            curr = curr.next


def removeDuplicates(ls) -> None:
    if not ls:
        return

    found = {ls.value}
    
    while ls.next is not None:
        if ls.next.value in found:
            ls.next = ls.next.next
        else:
            found.add(ls.next.value)
            ls = ls.next

ls = List.generate([1, 2, 3, 2, 4, 3])
ls.trace()
print()
removeDuplicates(ls)
ls.trace()