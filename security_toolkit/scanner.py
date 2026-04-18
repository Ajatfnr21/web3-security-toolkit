"""Web3 security scanner."""
import re
from typing import List, Dict

class SecurityScanner:
    """Scan for Web3 vulnerabilities."""
    
    def scan(self, code: str) -> List[Dict]:
        findings = []
        if 'tx.origin' in code:
            findings.append({'type': 'tx.origin usage', 'severity': 'critical'})
        return findings
