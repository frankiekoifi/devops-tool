#!/bin/bash


set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║     🔧 FRANKTECHSPACE - DEVOPS MONITORING TOOL 🔧         ║"
echo "║                                                           ║"
echo "║     Real-time system metrics & monitoring dashboard       ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check Python version
echo -e "${YELLOW}📌 Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✅ $PYTHON_VERSION found${NC}"
else
    echo -e "${RED}❌ Python 3 not found. Please install Python 3.8 or higher${NC}"
    exit 1
fi

# Create installation directory
INSTALL_DIR="$HOME/franktechspace-devops"
echo -e "${YELLOW}📁 Creating installation directory: $INSTALL_DIR${NC}"
mkdir -p "$INSTALL_DIR"
cd "$INSTALL_DIR"

# Clone or download the repository
echo -e "${YELLOW}📥 Downloading DevOps Tool...${NC}"
if [ -d "devops-tool" ]; then
    echo -e "${YELLOW}Updating existing installation...${NC}"
    cd devops-tool
    git pull origin main
else
    git clone https://github.com/frankiekoifi/devops-tool.git
    cd devops-tool
fi

# Create virtual environment
echo -e "${YELLOW}🐍 Creating Python virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo -e "${YELLOW}📦 Installing dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if not exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}📝 Creating configuration file...${NC}"
    cat > .env << EOF
# DevOps Tool Configuration
PORT=8001
HOST=0.0.0.0
DEBUG=False
EOF
fi

# Create start script
echo -e "${YELLOW}🚀 Creating start script...${NC}"
cat > start.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
python backend/app.py
EOF

chmod +x start.sh

echo -e "${GREEN}✅ Installation complete!${NC}"
echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🎉 DevOps Tool has been installed successfully!${NC}"
echo ""
echo -e "${YELLOW}📌 To start monitoring your computer:${NC}"
echo -e "   cd $INSTALL_DIR/devops-tool && ./start.sh"
echo ""
echo -e "${YELLOW}📌 Or run manually:${NC}"
echo -e "   cd $INSTALL_DIR/devops-tool"
echo -e "   source venv/bin/activate"
echo -e "   python backend/app.py"
echo ""
echo -e "${YELLOW}📌 Then open your browser to:${NC}"
echo -e "   http://localhost:8001"
echo ""
echo -e "${YELLOW}📌 To stop the tool:${NC}"
echo -e "   Press Ctrl+C in the terminal"
echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}💡 Need help? Contact: franktechspace@outlook.com${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"