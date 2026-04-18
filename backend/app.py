from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .monitor import monitor
from .pipeline import pipeline
from .alerts import alert_system
import datetime
import json

app = FastAPI(title="DevOps Automation Tool", description="CI/CD Pipeline with Monitoring & Alerts")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Background task to monitor system continuously
async def continuous_monitoring():
    """Background task that monitors system metrics"""
    import asyncio
    while True:
        try:
            metrics = monitor.get_current_metrics()
            alert_system.check_metrics(metrics)
            await asyncio.sleep(10)  # Check every 10 seconds
        except Exception as e:
            print(f"Monitoring error: {e}")
            await asyncio.sleep(30)

@app.on_event("startup")
async def startup_event():
    """Start background monitoring on server startup"""
    import asyncio
    asyncio.create_task(continuous_monitoring())
    print("=" * 50)
    print("🔧 DEVOPS AUTOMATION TOOL")
    print("=" * 50)
    print("📍 API: http://localhost:8001")
    print("📊 Monitoring: Active")
    print("🔄 CI/CD Pipeline: Ready")
    print("🔔 Alerts: Enabled")
    print("=" * 50)

# ============ MONITORING ENDPOINTS ============

@app.get("/api/monitor/current")
async def get_current_metrics():
    """Get current system metrics"""
    return monitor.get_current_metrics()

@app.get("/api/monitor/history")
async def get_metrics_history(hours: int = 24):
    """Get historical metrics"""
    return monitor.get_history(hours)

@app.get("/api/monitor/processes")
async def get_top_processes(limit: int = 10):
    """Get top processes by CPU usage"""
    return monitor.get_top_processes(limit)

@app.get("/api/monitor/info")
async def get_system_info():
    """Get system information"""
    return monitor.get_system_info()

# ============ CI/CD PIPELINE ENDPOINTS ============

@app.post("/api/pipeline/trigger")
async def trigger_pipeline(repo_url: str, branch: str = "main", auto_deploy: bool = True):
    """Trigger a new CI/CD pipeline run"""
    try:
        result = pipeline.run_pipeline(repo_url, branch, auto_deploy)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/pipeline/history")
async def get_pipeline_history(limit: int = 10):
    """Get recent pipeline runs"""
    return pipeline.get_recent_pipelines(limit)

@app.get("/api/pipeline/status/{pipeline_id}")
async def get_pipeline_status(pipeline_id: str):
    """Get status of a specific pipeline"""
    result = pipeline.get_pipeline_status(pipeline_id)
    if not result:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    return result

@app.get("/api/pipeline/stats")
async def get_pipeline_stats():
    """Get pipeline statistics"""
    return pipeline.get_deployment_stats()

# ============ ALERT ENDPOINTS ============

@app.get("/api/alerts")
async def get_alerts(active_only: bool = False):
    """Get all alerts"""
    if active_only:
        return alert_system.get_active_alerts()
    return alert_system.alerts

@app.post("/api/alerts/acknowledge/{alert_id}")
async def acknowledge_alert(alert_id: str):
    """Acknowledge an alert"""
    success = alert_system.acknowledge_alert(alert_id)
    if not success:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"message": "Alert acknowledged"}

@app.delete("/api/alerts/clear")
async def clear_alerts():
    """Clear all alerts"""
    alert_system.clear_alerts()
    return {"message": "All alerts cleared"}

@app.get("/api/alerts/summary")
async def get_alert_summary():
    """Get alert statistics"""
    return alert_system.get_alert_summary()

@app.get("/api/alerts/rules")
async def get_alert_rules():
    """Get configured alert rules"""
    return alert_system.alert_rules

# ============ DASHBOARD ENDPOINTS ============

@app.get("/api/dashboard")
async def get_dashboard_data():
    """Get all dashboard data in one request"""
    return {
        'metrics': monitor.get_current_metrics(),
        'system_info': monitor.get_system_info(),
        'alerts': alert_system.get_active_alerts(),
        'alert_summary': alert_system.get_alert_summary(),
        'recent_pipelines': pipeline.get_recent_pipelines(5),
        'pipeline_stats': pipeline.get_deployment_stats()
    }

# ============ HEALTH CHECK ============

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'services': {
            'monitor': 'active',
            'pipeline': 'active',
            'alerts': 'active'
        }
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        'name': 'DevOps Automation Tool',
        'version': '1.0.0',
        'endpoints': {
            'monitoring': '/api/monitor/current',
            'pipeline': '/api/pipeline/trigger',
            'alerts': '/api/alerts',
            'dashboard': '/api/dashboard',
            'docs': '/docs'
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)