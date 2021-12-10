import pytest
from main import (Parser, IncompleteLineException, CorruptedLineException,
                  get_middle_sorted)


def test_good_input():
    p = Parser()
    inputs = [
        "()",
        "[]",
        "([])",
        "{()()()}",
        "<([{}])>",
        "[<>({}){}[([])<>]]",
        "(((((((((())))))))))"
    ]
    for i in inputs:
        p.parse(i)


def test_bad_input():
    inputs = ["(]", "{()()()>", "(((()))}", "<([]){()}[{}])"]
    p = Parser()
    for i in inputs:
        with pytest.raises(CorruptedLineException):
            p.parse(i)


def test_parse_real_input():
    lines = [
        ("[({(<(())[]>[[{[]{<()<>>", IncompleteLineException, 0),
        ("[(()[<>])]({[<{<<[]>>(", IncompleteLineException, 0),
        ("{([(<{}[<>[]}>{[]{[(<()>", CorruptedLineException, 1197),
        ("(((({<>}<{<{<>}{[]{[]{}", IncompleteLineException, 0),
        ("[[<[([]))<([[{}[[()]]]", CorruptedLineException, 3),
        ("[{[{({}]{}}([{[{{{}}([]", CorruptedLineException, 57),
        ("{<[[]]>}<{[{[{[]{()[[[]", IncompleteLineException, 0),
        ("[<(<(<(<{}))><([]([]()", CorruptedLineException, 3),
        ("<{([([[(<>()){}]>(<<{{", CorruptedLineException, 25137),
        ("<{([{{}}[<[[[<>{}]]]>[]]", IncompleteLineException, 0),
    ]

    p = Parser()
    for ln, exc, count in lines:
        with pytest.raises(exc):
            p.parse(ln)
        assert p.count == count


def test_autocomplete_real_input():
    lines = [
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]", 288957),
        ("[(()[<>])]({[<{<<[]>>(", ")}>]})", 5566),
        ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))", 1480781),
        ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>", 995444),
        ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>", 294),
    ]
    p = Parser()
    for ln, cmpl, score in lines:
        with pytest.raises(IncompleteLineException):
            p.parse(ln)
        assert p.complete == cmpl
        assert p.autocomplete_score() == score


def test_get_middle_sorted():
    scores = [
        288957,
        5566,
        1480781,
        995444,
        294
    ]
    assert get_middle_sorted(scores) == 288957
