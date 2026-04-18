import subprocess
import json
import datetime
import os
import shutil
import random

class CICDPipeline:
    def __init__(self):
        self.pipeline_history = []
        self.deployments = []
        
    def run_pipeline(self, repo_url, branch='main', auto_deploy=True):
        """Run a complete CI/CD pipeline"""
        pipeline_id = f"PIPE-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        start_time = datetime.datetime.now()
        
        pipeline_data = {
            'id': pipeline_id,
            'repo_url': repo_url,
            'branch': branch,
            'start_time': start_time.isoformat(),
            'status': 'running',
            'stages': []
        }
        
        try:
            # Stage 1: Clone/Pull Repository
            stage1 = self._clone_repository(repo_url, branch)
            pipeline_data['stages'].append(stage1)
            
            if stage1['status'] == 'failed':
                raise Exception("Failed to clone repository")
            
            # Stage 2: Install Dependencies
            stage2 = self._install_dependencies()
            pipeline_data['stages'].append(stage2)
            
            if stage2['status'] == 'failed':
                raise Exception("Failed to install dependencies")
            
            # Stage 3: Run Tests
            stage3 = self._run_tests()
            pipeline_data['stages'].append(stage3)
            
            if stage3['status'] == 'failed':
                raise Exception("Tests failed")
            
            # Stage 4: Build Application
            stage4 = self._build_application()
            pipeline_data['stages'].append(stage4)
            
            if stage4['status'] == 'failed':
                raise Exception("Build failed")
            
            # Stage 5: Deploy (if auto_deploy is True)
            if auto_deploy:
                stage5 = self._deploy_application()
                pipeline_data['stages'].append(stage5)
                
                if stage5['status'] == 'failed':
                    raise Exception("Deployment failed")
            
            pipeline_data['status'] = 'success'
            pipeline_data['end_time'] = datetime.datetime.now().isoformat()
            
            # Record deployment
            if auto_deploy:
                self.deployments.append({
                    'id': pipeline_id,
                    'repo': repo_url,
                    'branch': branch,
                    'deployed_at': datetime.datetime.now().isoformat(),
                    'status': 'success'
                })
            
        except Exception as e:
            pipeline_data['status'] = 'failed'
            pipeline_data['error'] = str(e)
            pipeline_data['end_time'] = datetime.datetime.now().isoformat()
        
        # Calculate duration
        end = datetime.datetime.fromisoformat(pipeline_data['end_time'])
        start = datetime.datetime.fromisoformat(pipeline_data['start_time'])
        pipeline_data['duration_seconds'] = (end - start).total_seconds()
        
        # Store history
        self.pipeline_history.insert(0, pipeline_data)
        if len(self.pipeline_history) > 50:
            self.pipeline_history.pop()
        
        return pipeline_data
    
    def _clone_repository(self, repo_url, branch):
        """Clone or pull repository"""
        start = datetime.datetime.now()
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        
        try:
            if os.path.exists(repo_name):
                # Pull latest changes
                result = subprocess.run(
                    ['git', '-C', repo_name, 'pull', 'origin', branch],
                    capture_output=True, text=True, timeout=60
                )
            else:
                # Clone repository
                result = subprocess.run(
                    ['git', 'clone', '-b', branch, repo_url],
                    capture_output=True, text=True, timeout=120
                )
            
            return {
                'name': 'Clone Repository',
                'status': 'success' if result.returncode == 0 else 'failed',
                'duration': (datetime.datetime.now() - start).total_seconds(),
                'output': result.stdout if result.returncode == 0 else result.stderr
            }
        except Exception as e:
            return {
                'name': 'Clone Repository',
                'status': 'failed',
                'duration': (datetime.datetime.now() - start).total_seconds(),
                'output': str(e)
            }
    
    def _install_dependencies(self):
        """Install project dependencies"""
        start = datetime.datetime.now()
        
        # Simulate dependency installation
        # In real scenario, you'd run npm install or pip install
        import time
        time.sleep(2)  # Simulate work
        
        return {
            'name': 'Install Dependencies',
            'status': 'success',
            'duration': (datetime.datetime.now() - start).total_seconds(),
            'output': 'Installed 45 packages successfully'
        }
    
    def _run_tests(self):
        """Run automated tests"""
        start = datetime.datetime.now()
        
        # Simulate test execution
        import time
        time.sleep(3)  # Simulate work
        
        # Random test results (80% success rate for demo)
        passed = random.random() > 0.2
        
        return {
            'name': 'Run Tests',
            'status': 'success' if passed else 'failed',
            'duration': (datetime.datetime.now() - start).total_seconds(),
            'output': f'✅ 42 tests passed, 0 failed' if passed else '❌ 38 tests passed, 4 failed',
            'details': {
                'total': 42,
                'passed': 42 if passed else 38,
                'failed': 0 if passed else 4,
                'coverage': '85%'
            }
        }
    
    def _build_application(self):
        """Build the application"""
        start = datetime.datetime.now()
        
        # Simulate build process
        import time
        time.sleep(2)
        
        return {
            'name': 'Build Application',
            'status': 'success',
            'duration': (datetime.datetime.now() - start).total_seconds(),
            'output': 'Build completed successfully. Artifact size: 24.5 MB'
        }
    
    def _deploy_application(self):
        """Deploy to production/staging"""
        start = datetime.datetime.now()
        
        # Simulate deployment
        import time
        time.sleep(1.5)
        
        return {
            'name': 'Deploy Application',
            'status': 'success',
            'duration': (datetime.datetime.now() - start).total_seconds(),
            'output': 'Deployed to production at http://app.example.com'
        }
    
    def get_pipeline_status(self, pipeline_id):
        """Get status of a specific pipeline"""
        for pipeline in self.pipeline_history:
            if pipeline['id'] == pipeline_id:
                return pipeline
        return None
    
    def get_recent_pipelines(self, limit=10):
        """Get recent pipeline runs"""
        return self.pipeline_history[:limit]
    
    def get_deployment_stats(self):
        """Get deployment statistics"""
        if not self.deployments:
            return {'total': 0, 'success_rate': 0}
        
        successful = len([d for d in self.deployments if d['status'] == 'success'])
        return {
            'total': len(self.deployments),
            'successful': successful,
            'failed': len(self.deployments) - successful,
            'success_rate': (successful / len(self.deployments)) * 100
        }

# Create global pipeline instance
pipeline = CICDPipeline()