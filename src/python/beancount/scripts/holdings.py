"""Print out a list of current holdings, relative or absolute.

This is to share my portfolio with others, or to compute its daily changes.
"""
from beancount import load
from beancount.parser import options
from beancount.ops import prices
from beancount.ops import holdings
from beancount.ops import summarize


def main():
    import argparse
    optparser = argparse.ArgumentParser(__doc__)
    optparser.add_argument('filename', help='Filename.')

    optparser.add_argument('-s', '--brief', '--relative-only',
                           action='store_true',
                           help="Only display the relative value of the account.")

    optparser.add_argument('-f', '--format', default='txt',
                           choices=['txt', 'csv'],
                           help="Output format.")

    opts = optparser.parse_args()

    # Parse the input file.
    entries, errors, options_map = load(opts.filename, quiet=True)

    # Close the books.
    entries = summarize.close(entries, options_map,
                              *options.get_current_accounts(options_map))

    # Get the aggregate sum of holdings.
    price_map = prices.build_price_map(entries)
    holdings_list = holdings.get_final_holdings(entries, price_map)

    for h in holdings_list:
        print(h)

    # # Aggregate then..
    # byinst = dataframe.groupby(['account', 'currency', 'cost_currency'])
    # byinst_agg = byinst['number', 'market_value'].sum()
    # byinst_agg['avg_cost'] = byinst['cost_number'].mean()
    # byinst_agg['price_number'] = byinst['price_number'].mean()
    # byinst_agg = byinst_agg.sort('market_value', ascending=False)

    # # Compute the percentage.
    # total_value = byinst_agg['market_value'].sum()
    # byinst_agg['percent'] = byinst_agg['market_value'] / total_value

    # percent_only = byinst_agg[['percent']].sum(level=[1,2]).sort('percent', ascending=False)

    # if opts.format == 'txt':
    #     output = percent_only.to_string(formatters={'percent': '{:.1%}'.format})
    # elif opts.format == 'csv':
    #     output = percent_only.to_csv()
    # print(output)

    # ## FIXME: todo - implement --brief


if __name__ == '__main__':
    main()