def hasMatch(self, s: str, p: str) -> bool:
        star=p.find("*")
        pre=p[:star]
        suf=p[star+1:]
        prepos=s.find(pre)
        if prepos==-1:
            return False
        sufpos=s.find(suf,prepos + len(pre))
        return sufpos !=-1