# Simple On-Prem vs Cloud monthly cost comparison (edu-only)

def on_prem_cost(servers=2, server_monthly=350, power_cooling=120, admin=150):
    """
    servers: number of physical servers
    server_monthly: amortized monthly cost per server (capex/lease)
    power_cooling: electricity + cooling per server per month
    admin: per-server share of admin/maintenance/month
    """
    return servers * (server_monthly + power_cooling + admin)

def cloud_cost(instances=2, ec2_per_instance=90, storage_gb=200, s3_per_gb=0.023, data_egress_gb=50, egress_per_gb=0.09):
    """
    instances: number of EC2 instances
    ec2_per_instance: estimated monthly (on-demand) per instance
    storage_gb: S3 storage used
    s3_per_gb: S3 standard storage cost per GB-month
    data_egress_gb: monthly internet egress
    egress_per_gb: egress cost per GB (region-dependent)
    """
    compute = instances * ec2_per_instance
    storage = storage_gb * s3_per_gb
    egress  = data_egress_gb * egress_per_gb
    return compute + storage + egress

def explain(op, cl):
    diff = op - cl
    verdict = "Cloud cheaper" if diff > 0 else "On-prem cheaper"
    return diff, verdict

if __name__ == "__main__":
    # Example scenario (adjust freely)
    op = on_prem_cost(servers=2, server_monthly=350, power_cooling=120, admin=150)
    cl = cloud_cost(instances=2, ec2_per_instance=90, storage_gb=200, s3_per_gb=0.023, data_egress_gb=50, egress_per_gb=0.09)

    diff, verdict = explain(op, cl)

    print("=== Monthly Cost Estimate (Educational) ===")
    print(f"On-Prem Total : ${op:,.2f}")
    print(f"Cloud Total   : ${cl:,.2f}")
    print(f"Difference    : ${abs(diff):,.2f}  ({'on-prem minus cloud' if diff>0 else 'cloud minus on-prem'})")
    print(f"Verdict       : {verdict}")
    print("\nNotes:")
    print("- Numbers are rough and simplified (no RI/Savings Plans, support, backups, staff salaries, etc.).")
    print("- Real decisions require TCO, reliability, scaling, and compliance considerations.")
