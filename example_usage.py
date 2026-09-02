from client import CreatorPaidAmplificationRoiSynthesizerClient

def main():
    client = CreatorPaidAmplificationRoiSynthesizerClient()
    res = client.calculate_paid_spark_roi('https://tiktok.com/@creator/video/1', 2000.00, 9400.00)
    print('Creator Paid Amplification ROI Synthesizer: ' + res['amplification_synthesis_id'])
    print('ROAS Multiplier: ' + str(res['organic_to_paid_roas_multiplier']) + 'x | Blended CAC: $' + str(res['blended_customer_acquisition_cost_cac_usd']))
    print('Conversion Lift: +' + str(res['spark_ad_conversion_lift_vs_brand_standard_pct']) + '%')
    print('Analytics Dossier: ' + res['paid_amplification_analytics_dossier_url'])

if __name__ == '__main__':
    main()
