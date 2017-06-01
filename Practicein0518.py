# 这是Python构建命令行的学习，参考链接：http://mp.weixin.qq.com/s/t_TvUmfkp3R89kek5lQ28w特此致谢


def repl():
    from prompt_toolkit import prompt
    while 1:
        user_input = prompt('>')
        print(user_input)


def history():
    from prompt_toolkit import prompt
    from prompt_toolkit.history import FileHistory
    while 1:
        user_input = prompt('>',
                            history=FileHistory('history.txt'),
                            )
        print(user_input)


def autoSug():
    from prompt_toolkit import prompt
    from prompt_toolkit.history import FileHistory
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
    while 1:
        user_input = prompt('>',
                            history=FileHistory('historyas.txt'),
                            auto_suggest=AutoSuggestFromHistory(),
                            )
        print(user_input, ...)


def completers():
    from prompt_toolkit import prompt
    from prompt_toolkit.history import History
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
    from prompt_toolkit.contrib.completers import WordCompleter
    import click

    SQLCompleter = WordCompleter(['select', 'from', 'insert', 'update', 'delete', 'drop'],
                                 ignore_case=True)
    while 1:
        user_input = prompt('SQL>',
                            history=FileHistory('historysc.txt'),
                            auto_suggest=AutoSuggestFromHistory(),
                            completer=SQLCompleter,
                            )
        # print(user_input, ...)
        click.echo_via_pager(user_input)


def clickUsage():
    import click
    message = click.edit()


def simpleFuzzyFinder():
    from fuzzyfinder import fuzzyfinder
    suggestion = fuzzyfinder(
        'abc', ['abcd', 'defabca', 'aagbec', 'xyz', 'qux'])
    print(list(suggestion), ...)


from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
import click
from fuzzyfinder import fuzzyfinder
from pygments.lexers.sql import SqlLexer

SQLKeywords = ['select', 'from', 'insert', 'update', 'delete', 'drop']

class SQLCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, SQLKeywords)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))
            while 1:
                user_input = prompt(u'SQL>',
                                    history=FileHistory('historyff.txt'),
                                    auto_suggest=AutoSuggestFromHistory(),
                                    completer=SQLCompleter(),
                                    lexer = SqlLexer,
                                    )
                click.echo_via_pager(user_input)


