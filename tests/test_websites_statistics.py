import logging
import pytest
import pandas as pd

from pytest_check import check

from src.pages.test.page import WebsiteProgrammingLanguages


class Column:
    VISITORS = "Popularity (unique visitors per month)[1]"
    WEBSITES = "Websites"
    FRONTEND = "Front-end (Client-side)"
    BACKEND = "Back-end (Server-side)"


@pytest.fixture(scope="class")
def dataframe(request):
    homepage = WebsiteProgrammingLanguages(request.cls.driver)
    homepage.open()

    raw_tabel = homepage.get_result_table()
    html = raw_tabel.get_attribute('outerHTML')

    dfs = pd.read_html(html)
    df = dfs[0]

    df[Column.VISITORS] = df[Column.VISITORS].str.replace('[^0-9]', '', regex=True).astype(
        'int64')

    return df


@pytest.mark.usefixtures("setup")
class TestCustomers:
    logger = logging.getLogger()

    @pytest.mark.parametrize("expected_visitors",
                             [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
    def test_wiki(self, dataframe, expected_visitors):
        for index, row in dataframe.iterrows():
            visitors = row[Column.VISITORS]
            website = row[Column.WEBSITES]
            fe = row[Column.FRONTEND]
            be = row[Column.BACKEND]
            assertion_message = f'{website} (Frontend:{fe}|Backend:{be}) has {visitors} ' \
                                f'unique visitors per month. (Expected more than {int(expected_visitors)})'
            check.less(expected_visitors, visitors, assertion_message)
