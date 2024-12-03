import json
import os
from datetime import datetime, timedelta
import requests
import re

def get_vps_data():
    """获取VPS数据"""
    vps_services = [
        {
            "name": "Wap_TW",
            "cost": 1,
            "currency": "USD",
            "monthlyExpireDay": 3,
            "color": "primary",
            "url": "https://google.com"
        },
        {
            "name": "V.PS_MaoYanZu_SJC",
            "cost": 32.95,
            "currency": "EUR",
            "expireDate": "2025-2-1",
            "color": "danger",
            "url": "https://swasnext.console.aliyun.com/"
        },
        {
            "name": "VirMAch_JP_8.88",
            "cost": 8.88,
            "currency": "USD",
            "expireDate": "2025-3-8",
            "color": "primary",
            "url": "https://vps.hosting/clientarea/"
        },
        {
            "name": "Aliyun_SZ",
            "cost": 99,
            "currency": "CNY",
            "expireDate": "2025-3-15",
            "color": "danger",
            "url": "https://ca.ovh.com/manager/#/hub"
        },
        {
            "name": "Netcup_1o",
            "cost": 10,
            "currency": "EUR",
            "expireDate": "2025-9-9",
            "color": "success",
            "url": "https://billing.raksmart.com/whmcs/clientarea.php?action=products"
        },
        {
            "name": "Locvps_HK",
            "cost": 80,
            "currency": "CNY",
            "expireDate": "2025-9-27",
            "color": "success",
            "url": "https://us.ovhcloud.com/vps/"
        },
        {
            "name": "KuxueYun_BJ",
            "cost": 7.99,
            "currency": "USD",
            "expireDate": "2025-11-6",
            "color": "warning",
            "url": "https://my.frantech.ca/cart.php?gid=39"
        },
        {
            "name": "KuxueYun_US",
            "cost": 7.5,
            "currency": "USD",
            "expireData": "2025-11-29",
            "color": "info",
            "url": "https://www.customercontrolpanel.de/index.php?action=se"
        }
    ]
    
    # 计算北京时间
    utc_time = datetime.utcnow()
    beijing_time = utc_time + timedelta(hours=8)
    update_time = beijing_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"生成更新时间 (北京时间): {update_time}")
    
    return {
        "services": vps_services,
        "lastUpdate": update_time
    }

def update_html_file():
    """更新HTML文件中的数据"""
    try:
        data = get_vps_data()
        
        print("正在读取 index.html...")
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        print("原始文件大小:", len(html_content))
        
        # 更新VPS数据
        vps_data_str = json.dumps(data['services'], ensure_ascii=False, indent=4)
        
        # 使用正则表达式替换 vpsServices 数组内容
        pattern = r'const\s+vpsServices\s*=\s*\[([\s\S]*?)\]\s*;'
        new_content = re.sub(pattern, f'const vpsServices = {vps_data_str};', html_content)
        
        # 更新最后更新时间
        if '<div class="last-update text-center mb-3">' in html_content:
            # 如果已存在更新时间，则替换它
            new_content = re.sub(
                r'<div class="last-update text-center mb-3">.*?</div>',
                f'<div class="last-update text-center mb-3">最后更新时间: {data["lastUpdate"]}</div>',
                new_content
            )
        else:
            # 如果不存在，则在标题后添加
            new_content = new_content.replace(
                '</h1>',
                f'</h1>\n        <div class="last-update text-center mb-3">最后更新时间: {data["lastUpdate"]}</div>'
            )
        
        print("新文件大小:", len(new_content))
        
        print("正在写入更新后的文件...")
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print("文件更新完成")
        
    except Exception as e:
        print(f"更新失败: {str(e)}")
        raise

if __name__ == "__main__":
    update_html_file() 
