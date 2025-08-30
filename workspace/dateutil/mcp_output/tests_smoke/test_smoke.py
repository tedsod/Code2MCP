import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def test_imports():
    """Test basic imports"""
    try:
        from src.dateutil import parser, tz, relativedelta  # noqa: F401
        print("OK - Successfully imported src.dateutil")
        return True
    except Exception as e:
        print(f"Failed to import src.dateutil: {e}")
        return False

def test_package_imports():
    """Test package imports"""
    packages = ["src.dateutil.parser", "src.dateutil.tz", "src.dateutil.relativedelta"]
    success_count = 0
    
    for pkg in packages:
        try:
            __import__(pkg)
            print(f"OK - Successfully imported {pkg}")
            success_count += 1
        except Exception as e:
            print(f"Failed to import {pkg}: {e}")
    
    if success_count > 0:
        print(f"Successfully imported {success_count}/{len(packages)} packages")
        return True
    else:
        print("All import attempts failed")
        return False

if __name__ == "__main__":
    print("Running smoke tests...")
    
    test1 = test_imports()
    test2 = test_package_imports()
    
    if test1 and test2:
        print("All smoke tests passed")
        sys.exit(0)
    else:
        print("Some smoke tests failed")
        sys.exit(1)
