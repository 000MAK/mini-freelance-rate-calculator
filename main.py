import argparse

def evaluate(price, platform_fee, direct_cost, revision_reserve, minutes, floor=30.0):
    nums=[price,platform_fee,direct_cost,revision_reserve,floor]
    if any(x<0 for x in nums): raise ValueError("Amounts and floor must be non-negative")
    if minutes<=0: raise ValueError("Minutes must be positive")
    net=price-platform_fee-direct_cost-revision_reserve
    rate=net*60/minutes
    return {"estimated_net":round(net,2),"hourly_rate":round(rate,2),"decision":"CONSIDER" if rate>=floor else "BELOW_FLOOR"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--price",type=float,required=True); ap.add_argument("--fee",type=float,default=0); ap.add_argument("--cost",type=float,default=0); ap.add_argument("--reserve",type=float,default=0); ap.add_argument("--minutes",type=float,required=True); ap.add_argument("--floor",type=float,default=30); a=ap.parse_args()
    r=evaluate(a.price,a.fee,a.cost,a.reserve,a.minutes,a.floor); print(f"Estimated net before taxes/fixed overhead: ${r['estimated_net']:.2f}\nEstimated hourly: ${r['hourly_rate']:.2f}\nDecision: {r['decision']}")
if __name__=="__main__": main()
