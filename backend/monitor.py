import psutil
import platform
import datetime
import os

class SystemMonitor:
    def __init__(self):
        self.history = []
        self.max_history = 100  # Keep last 100 readings
        
    def get_system_info(self):
        """Get basic system information"""
        return {
            'hostname': platform.node(),
            'os': platform.system(),
            'os_version': platform.version(),
            'python_version': platform.python_version(),
            'cpu_count': psutil.cpu_count(),
            'uptime': datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
        }
    
    def get_current_metrics(self):
        """Get current system metrics"""
        # CPU metrics
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_per_core = psutil.cpu_percent(percpu=True)
        
        # Memory metrics
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        # Disk metrics
        disk = psutil.disk_usage('/')
        
        # Network metrics
        network = psutil.net_io_counters()
        
        # Process metrics
        processes = len(psutil.pids())
        
        metrics = {
            'timestamp': datetime.datetime.now().isoformat(),
            'cpu': {
                'overall': cpu_percent,
                'per_core': cpu_per_core,
                'status': 'critical' if cpu_percent > 90 else 'warning' if cpu_percent > 70 else 'healthy'
            },
            'memory': {
                'total': memory.total,
                'available': memory.available,
                'used': memory.used,
                'percentage': memory.percent,
                'swap_used': swap.used,
                'swap_percent': swap.percent,
                'status': 'critical' if memory.percent > 90 else 'warning' if memory.percent > 75 else 'healthy'
            },
            'disk': {
                'total': disk.total,
                'used': disk.used,
                'free': disk.free,
                'percentage': disk.percent,
                'status': 'critical' if disk.percent > 90 else 'warning' if disk.percent > 80 else 'healthy'
            },
            'network': {
                'bytes_sent': network.bytes_sent,
                'bytes_recv': network.bytes_recv,
                'packets_sent': network.packets_sent,
                'packets_recv': network.packets_recv
            },
            'processes': processes,
            'overall_status': 'healthy'
        }
        
        # Determine overall status
        statuses = [metrics['cpu']['status'], metrics['memory']['status'], metrics['disk']['status']]
        if 'critical' in statuses:
            metrics['overall_status'] = 'critical'
        elif 'warning' in statuses:
            metrics['overall_status'] = 'warning'
        else:
            metrics['overall_status'] = 'healthy'
        
        # Store history
        self.history.append(metrics)
        if len(self.history) > self.max_history:
            self.history.pop(0)
        
        return metrics
    
    def get_history(self, hours=24):
        """Get historical metrics for last X hours"""
        cutoff = datetime.datetime.now() - datetime.timedelta(hours=hours)
        return [m for m in self.history if datetime.datetime.fromisoformat(m['timestamp']) > cutoff]
    
    def get_top_processes(self, n=10):
        """Get top N processes by CPU usage"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pinfo = proc.info
                pinfo['cpu_percent'] = proc.cpu_percent(interval=0.1)
                processes.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        processes.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
        return processes[:n]

# Create global monitor instance
monitor = SystemMonitor()