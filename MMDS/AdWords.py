__author__ = 'Tong'

# 5A2


class Advertiser:
    name = ''
    bid = 0
    ctr = [0] * 3
    budget = 0
    clicks = 0

    def __init__(self, name, bid, ctr, budget):
        self.name = name
        self.bid = bid
        self.ctr = ctr
        self.budget = budget

    def __str__(self):
        return "Advertiser " + self.name + " : remaining budget " + round(self.budget,
                                                                          2).__str__() + ", got " + self.clicks.__str__() + " clicks."


def init_test_set():
    advertisers = [Advertiser('A', 0.10, [0.015, 0.010, 0.005], 1),
                   Advertiser('B', 0.09, [0.016, 0.012, 0.006], 2),
                   Advertiser('C', 0.08, [0.017, 0.014, 0.007], 3),
                   Advertiser('D', 0.07, [0.018, 0.015, 0.008], 4),
                   Advertiser('E', 0.06, [0.019, 0.016, 0.010], 5)]
    clicks = 101
    return advertisers, clicks


def ad_words():
    advertisers, clicks = init_test_set()

    slots = [None] * 3

    rou = 0

    # each phase
    while clicks > 0:
        print("Round " + rou.__str__() + ":")

        # assign advertisers to each slot considering their bids
        for s in range(len(slots)):
            opt_bid = 0
            opt_advertiser = None
            for advertiser in advertisers:
                bid = advertiser.bid * advertiser.ctr[s]
                if advertiser not in slots and opt_bid < bid <= advertiser.budget:
                    opt_bid = bid
                    opt_advertiser = advertiser
            slots[s] = opt_advertiser
        print("++Advertisers assigned.")
        for slot in slots:
            print(slot)

        # calculate total clicks that will be used in this round
        affordable_clicks = [0] * 3
        for s in range(len(slots)):
            affordable_clicks[s] = slots[s].budget / slots[s].bid / slots[s].ctr[s]
        total_clicks = min(affordable_clicks)

        # run the bidding until one advertiser run out of budget
        for s in range(len(slots)):
            each_clicks = int(total_clicks * slots[s].ctr[s])
            slots[s].budget -= each_clicks * slots[s].bid
            slots[s].clicks += each_clicks
            clicks -= each_clicks

        print("++Clicks assigned.")
        for slot in slots:
            print(slot)

        rou += 1
    print("\n\n++All clicks obtained.")
    for advertiser in advertisers:
        print(advertiser)


ad_words()