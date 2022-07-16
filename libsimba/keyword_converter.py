import keyword
# to avoid param and method name collision

ts_keywords = [
    "break",
    "case",
    "catch",
    "class",
    "const",
    "continue",
    "debugger",
    "default",
    "delete",
    "do",
    "else",
    "enum",
    "export",
    "extends",
    "false",
    "finally",
    "for",
    "function",
    "if",
    "import",
    "in",
    "instanceof",
    "new",
    "null",
    "return",
    "super",
    "switch",
    "this",
    "throw",
    "true",
    "try",
    "typeof",
    "var",
    "void",
    "while",
    "with",
    "as",
    "implements",
    "interface",
    "let",
    "package",
    "private",
    "protected",
    "public",
    "static",
    "yield",
    "any",
    "boolean",
    "constructor",
    "declare",
    "get",
    "module",
    "require",
    "number",
    "set",
    "string",
    "symbol",
    "type",
    "from",
    "of",
]

java_keywords = [ 
    "abstract",
    "assert",
    "boolean",
    "break",
    "byte",
    "case",
    "catch",
    "char",
    "class",
    "const",
    "continue",
    "default",
    "do",
    "double",
    "else",
    "enum",
    "extends",
    "final",
    "finally",
    "float",
    "for",
    "goto",
    "if",
    "implement",
    "imports",
    "instanceof",
    "int",
    "interface",
    "long",
    "native",
    "new",
    "package",
    "private",
    "protected",
    "public",
    "return",
    "short",
    "static",
    "strictfp",
    "super",
    "switch",
    "synchronized",
    "this",
    "throw",
    "throws",
    "transient",
    "try",
    "void",
    "volatile",
    "while",
    "false",
    "null",
    "true",
]

golang_keywords = [
    "break",
    "case",
    "chan",
    "const",
    "continue",
    "default",
    "defer",
    "else",
    "fallthrough",
    "for",
    "func",
    "go",
    "goto",
    "if",
    "import",
    "interface",
    "map",
    "package",
    "range",
    "return",
    "select",
    "struct",
    "switch",
    "type",
    "var",
]

class KeywordConverter:
    def __init__(self, language: str = None):
        self.language = language.lower()
        self.keyword_dict = self.keyword_conversion()
    
    def keyword_conversion(self):
        if self.language.lower() == "python":
            kw_dict = {}
            for kw in keyword.kwlist:
                if kw[0].isupper():
                    kw_dict[kw] = kw[0].lower() + kw[1:]
                else:
                    kw_dict[kw] = kw[0].upper() + kw[1:]
            return kw_dict
        if self.language.lower() == "typescript":
            kw_dict = {}
            for kw in ts_keywords:
                kw_dict[kw] = kw[0].upper() + kw[1:]
            return kw_dict
        if self.language.lower() == "java":
            kw_dict = {}
            for kw in java_keywords:
                kw_dict[kw] = kw[0].upper() + kw[1:]
            return kw_dict
        if self.language.lower() == "golang":
            kw_dict = {}
            for kw in golang_keywords:
                kw_dict[kw] = kw[0].upper() + kw[1:]
            return kw_dict
    
    def convert_keyword(self, word: str):
        if self.language == "python":
            if word.startswith("__"):
                word = word[2:]
        if word in self.keyword_dict:
            return self.keyword_dict[word]
        else:
            return word