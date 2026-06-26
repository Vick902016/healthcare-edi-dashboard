# 🏥 Healthcare EDI Dashboard

A real-time monitoring dashboard for tracking daily healthcare Electronic Data Interchange (EDI) file transmissions. Built with Streamlit, this dashboard provides visibility into scheduled jobs, transmission status, and error investigation tools.

## Overview

The **Healthcare EDI Dashboard** monitors healthcare data exchanges across three job types (D1, D2, D3), tracking inbound and outbound transmissions from multiple clinical clients. The dashboard provides:

- **Real-time KPIs**: Track total jobs, failures, and SLA success rates
- **Job Execution Logs**: Filter and view transmission details by job type
- **Error Investigation**: Drill into failed jobs with detailed error logs and system diagnostics

## Features

### System Overview
- **Total Jobs Today**: Count of all scheduled transmissions
- **Failed Transmissions**: Number of jobs that encountered errors
- **SLA Success Rate**: Calculated percentage of successful transmissions

### Job Execution Logs
- Interactive data table with job details
- Filter by job type (D1, D2, D3)
- View client names, transmission direction, scheduled time, and status

### Escalation & Error Investigation
- Expandable error investigation panels for failed jobs
- Raw error logs with diagnostic information
- Simulated retry notifications

## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Fast, interactive web app framework
- **Data Processing**: [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- **Database**: SQLite - Lightweight, embedded database for job tracking
- **Language**: Python 3.x

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vick902016/healthcare-edi-dashboard.git
   cd healthcare-edi-dashboard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

### How It Works

1. **Database Initialization**: On startup, `setup_db.py` generates mock EDI job data
2. **Data Refresh**: Each page load creates fresh mock data (15 jobs per session)
3. **Dashboard Display**: Real-time metrics and interactive filtering
4. **Error Analysis**: Click expanders to investigate failed transmissions

## Project Structure

```
healthcare-edi-dashboard/
├── app.py              # Main Streamlit application
├── setup_db.py         # Database setup and mock data generation
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Data Schema

The dashboard tracks jobs with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `job_id` | TEXT | Job identifier (D1, D2, D3) |
| `client_name` | TEXT | Healthcare client name |
| `direction` | TEXT | Transmission type (Inbound HL7, Outbound 837P) |
| `scheduled_time` | TEXT | Time job was scheduled (HH:MM format) |
| `status` | TEXT | Job status (Success or Failed) |
| `error_log` | TEXT | Error message if status is Failed |

## Mock Data Characteristics

- **Jobs Generated**: 15 per session
- **Success Rate**: ~80% (20% failure rate for demonstration)
- **Clients**: Client Alpha, Client Beta, Client Gamma
- **Directions**: Inbound HL7 messages, Outbound 837P claims
- **Sample Errors**:
  - HTTP 408: Request Timeout
  - SSL Certificate Expiration
  - Invalid JSON Payload Format

## Future Enhancements

- [ ] Connect to real healthcare EDI systems (HL7, X12 standards)
- [ ] Persistent database with historical tracking
- [ ] Email alerts for failed transmissions
- [ ] Performance analytics and trend analysis
- [ ] Client-specific dashboards
- [ ] SLA compliance reporting
- [ ] Automated retry mechanisms with exponential backoff
- [ ] Multi-user authentication

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/Vick902016/healthcare-edi-dashboard/issues).

---

**Note**: This dashboard uses mock data for demonstration purposes. Production implementations should integrate with actual healthcare EDI systems and secure data sources.
