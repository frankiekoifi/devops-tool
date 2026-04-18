import datetime
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AlertSystem:
    def __init__(self):
        self.alerts = []
        self.alert_rules = []
        self.notification_channels = []
        
        # Default alert rules
        self.alert_rules = [
            {
                'id': 'cpu_high',
                'name': 'High CPU Usage',
                'condition': lambda m: m['cpu']['overall'] > 85,
                'severity': 'warning',
                'message': 'CPU usage is above 85%'
            },
            {
                'id': 'cpu_critical',
                'name': 'Critical CPU Usage',
                'condition': lambda m: m['cpu']['overall'] > 95,
                'severity': 'critical',
                'message': 'CPU usage is CRITICAL at {value}%'
            },
            {
                'id': 'memory_high',
                'name': 'High Memory Usage',
                'condition': lambda m: m['memory']['percentage'] > 85,
                'severity': 'warning',
                'message': 'Memory usage is above 85%'
            },
            {
                'id': 'memory_critical',
                'name': 'Critical Memory Usage',
                'condition': lambda m: m['memory']['percentage'] > 95,
                'severity': 'critical',
                'message': 'Memory usage is CRITICAL at {value}%'
            },
            {
                'id': 'disk_high',
                'name': 'High Disk Usage',
                'condition': lambda m: m['disk']['percentage'] > 85,
                'severity': 'warning',
                'message': 'Disk usage is above 85%'
            },
            {
                'id': 'disk_critical',
                'name': 'Critical Disk Usage',
                'condition': lambda m: m['disk']['percentage'] > 95,
                'severity': 'critical',
                'message': 'Disk usage is CRITICAL at {value}%'
            }
        ]
        
        # Default notification channels (console only for demo)
        self.notification_channels = ['console']
    
    def check_metrics(self, metrics):
        """Check metrics against alert rules"""
        triggered_alerts = []
        
        for rule in self.alert_rules:
            try:
                if rule['condition'](metrics):
                    alert = {
                        'id': f"{rule['id']}_{datetime.datetime.now().timestamp()}",
                        'rule_id': rule['id'],
                        'name': rule['name'],
                        'severity': rule['severity'],
                        'message': rule['message'].format(
                            value=metrics['cpu']['overall'] if 'cpu' in rule['message'] 
                            else metrics['memory']['percentage'] if 'memory' in rule['message']
                            else metrics['disk']['percentage']
                        ),
                        'metrics': metrics,
                        'timestamp': datetime.datetime.now().isoformat(),
                        'acknowledged': False
                    }
                    
                    triggered_alerts.append(alert)
                    self.alerts.insert(0, alert)
                    
                    # Send notification
                    self.send_notification(alert)
            except Exception as e:
                print(f"Error checking rule {rule['id']}: {e}")
        
        # Keep only last 100 alerts
        if len(self.alerts) > 100:
            self.alerts = self.alerts[:100]
        
        return triggered_alerts
    
    def send_notification(self, alert):
        """Send alert notification to configured channels"""
        message = f"[{alert['severity'].upper()}] {alert['name']}: {alert['message']}"
        
        for channel in self.notification_channels:
            if channel == 'console':
                print(f"🔔 ALERT: {message}")
            elif channel == 'slack':
                self._send_slack_alert(alert)
            elif channel == 'email':
                self._send_email_alert(alert)
    
    def _send_slack_alert(self, alert):
        """Send alert to Slack webhook"""
        webhook_url = os.getenv('SLACK_WEBHOOK_URL')
        if webhook_url:
            payload = {
                'text': f"*[DevOps Alert]*\n{alert['name']}\n{alert['message']}\nSeverity: {alert['severity']}",
                'username': 'DevOps Monitor'
            }
            try:
                requests.post(webhook_url, json=payload)
            except:
                pass
    
    def _send_email_alert(self, alert):
        """Send alert via email"""
        # Email configuration would go here
        # This is a placeholder for demo
        pass
    
    def get_active_alerts(self):
        """Get unacknowledged alerts"""
        return [a for a in self.alerts if not a.get('acknowledged', False)]
    
    def acknowledge_alert(self, alert_id):
        """Mark alert as acknowledged"""
        for alert in self.alerts:
            if alert['id'] == alert_id:
                alert['acknowledged'] = True
                alert['acknowledged_at'] = datetime.datetime.now().isoformat()
                return True
        return False
    
    def clear_alerts(self):
        """Clear all alerts"""
        self.alerts = []
    
    def add_notification_channel(self, channel_type, config):
        """Add a notification channel"""
        self.notification_channels.append({
            'type': channel_type,
            'config': config
        })
    
    def get_alert_summary(self):
        """Get alert statistics"""
        total = len(self.alerts)
        critical = len([a for a in self.alerts if a['severity'] == 'critical'])
        warning = len([a for a in self.alerts if a['severity'] == 'warning'])
        acknowledged = len([a for a in self.alerts if a.get('acknowledged', False)])
        
        return {
            'total': total,
            'critical': critical,
            'warning': warning,
            'acknowledged': acknowledged,
            'unresolved': total - acknowledged
        }

# Create global alert system
alert_system = AlertSystem()