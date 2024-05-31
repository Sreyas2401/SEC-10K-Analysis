from sec_edgar_downloader import Downloader

dl = Downloader("UMASS", "srajasekharu@umass.edu")

def get_filings_previous(ticker):
    dl.get('10-K', ticker, after='1995-01-01', before='2023-12-31', download_details=True)
    print(f'download complete - {ticker}')

def get_filings(ticker):
    dl.get('10-K', ticker, limit=1, download_details=True)
    print(f'download complete - {ticker}')

#get_filings('ETSY')
