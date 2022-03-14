class Solution:
    def simplifyPath(self, path: str) -> str:
        canon_dirs = []
        for pathdir in filter(lambda x: x != '.' and x != '', path.split(sep='/')):
            if pathdir == '..':
                if canon_dirs:
                    del canon_dirs[-1]
            else:
                canon_dirs.append(pathdir)
        return '/' + '/'.join(canon_dirs)
