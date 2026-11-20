#!/usr/bin/env python3
import sys
import json
import argparse

def calculate_base_metrics(spend, revenue):
    if spend <= 0:
        return {"roas": 0.0, "roi": 0.0}
    roas = round(revenue / spend, 2)
    roi = round(((revenue - spend) / spend) * 100, 2)
    return {"roas": roas, "roi": roi}

def project_scale(current_spend, target_spend, current_roas, decay_factor=0.85):
    if current_spend <= 0 or target_spend <= 0 or current_roas <= 0:
        return {"projected_roas": 0.0, "projected_revenue": 0.0, "efficiency_loss": 0.0}
    spend_ratio = target_spend / current_spend
    projected_roas = round(current_roas * (spend_ratio ** (decay_factor - 1)), 2)
    projected_revenue = round(target_spend * projected_roas, 2)
    efficiency_loss = round((1 - (projected_roas / current_roas)) * 100, 2)
    return {
        "projected_roas": projected_roas,
        "projected_revenue": projected_revenue,
        "efficiency_loss": efficiency_loss
    }

def main():
    parser = argparse.ArgumentParser(description="TAVARDT USA: Paid Media ROI Intelligence and Budget Scaling Engine")
    parser.add_argument("--spend", type=float, required=True, help="Current ad spend (USD)")
    parser.add_argument("--revenue", type=float, required=True, help="Current generated revenue (USD)")
    parser.add_argument("--target-spend", type=float, help="Projected target ad spend (USD)")
    parser.add_argument("--decay", type=float, default=0.85, help="Diminishing returns decay coefficient (default: 0.85)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    base = calculate_base_metrics(args.spend, args.revenue)
    target_spend = args.target_spend or (args.spend * 2.0)
    scale = project_scale(args.spend, target_spend, base["roas"], args.decay)

    if args.json:
        payload = {
            "currency": "USD",
            "current_spend": args.spend,
            "current_revenue": args.revenue,
            "base_metrics": base,
            "scaling_projection": {
                "target_spend": target_spend,
                "decay_factor": args.decay,
                "projection": scale
            }
        }
        print(json.dumps(payload, indent=2))
        return

    border = "=" * 74
    print(border)
    print(f" TAVARDT USA: PAID MEDIA ROI INTELLIGENCE AND BUDGET SCALING ENGINE")
    print(border)
    print(f" Current Media Spend: USD {args.spend:,.2f}")
    print(f" Generated Revenue: USD {args.revenue:,.2f}")
    print(f" Base ROAS: {base['roas']:.2f}x")
    print(f" Base ROI: {base['roi']:.2f}%")
    print("-" * 74)
    print(f" SCALING FORECAST (DIMINISHING RETURNS COEFFICIENT: {args.decay})")
    print(f" Projected Target Spend: USD {target_spend:,.2f}")
    print(f" Projected ROAS (Diminishing Returns): {scale['projected_roas']:.2f}x")
    print(f" Projected Revenue: USD {scale['projected_revenue']:,.2f}")
    print(f" Marginal Efficiency Loss: {scale['efficiency_loss']:.2f}%")
    print(border)

if __name__ == "__main__":
    main()
