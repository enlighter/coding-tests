using System;
using System.Runtime.CompilerServices;

// whitespace detection method: very fast, a lot faster than Char.IsWhiteSpace
[MethodImpl(MethodImplOptions.AggressiveInlining)] // if it's not inlined then it will be slow!!!
public static bool isWhiteSpace(char ch)
{
    switch (ch)
    {
        case '\u0009':
        case '\u000A':
        case '\u000B':
        case '\u000C':
        case '\u000D':
        case '\u0020':
        case '\u0085':
        case '\u00A0':
        case '\u1680':
        case '\u2000':
        case '\u2001':
        case '\u2002':
        case '\u2003':
        case '\u2004':
        case '\u2005':
        case '\u2006':
        case '\u2007':
        case '\u2008':
        case '\u2009':
        case '\u200A':
        case '\u2028':
        case '\u2029':
        case '\u202F':
        case '\u205F':
        case '\u3000':
            return true;
        default:
            return false;
    }
}

public static string TrimAllWhitespaces(string str)
{
    var len = str.Length;
    var src = str.ToCharArray();
    int dstIdx = 0;
    for (int i = 0; i < len; i++)
    {
        var ch = src[i];
        if (!isWhiteSpace(ch))
            src[dstIdx++] = ch;
    }
    return new string(src, 0, dstIdx);
}
