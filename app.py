import streamlit as st
import pandas as pd
import sqlite3

# 1. Page Configuration
st.set_page_config(page_title="Healthcare EDI Dashboard", layout="wide")
st.title("🏥 Daily File Transmission Monitor (D1, D2, D3)")

# 2. Fetch Data via SQL
def load_data():
    conn = sqlite3.connect('healthcare_jobs.db')
    query = "SELECT * FROM daily_jobs"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

data = load_data()

# 3. High-Level KPIs
st.subheader("System Overview")
total_jobs = len(data)
failed_jobs = len(data[data['status'] == 'Failed'])
success_rate = ((total_jobs - failed_jobs) / total_jobs) * 100

col1, col2, col3 = st.columns(3)
col1.metric("Total Jobs Today", total_jobs)
col2.metric("Failed Transmissions", failed_jobs, delta_color="inverse")
col3.metric("SLA Success Rate", f"{success_rate:.1f}%")

st.divider()

# 4. Interactive Data Table
st.subheader("Job Execution Logs")
job_filter = st.selectbox("Filter by Job ID:", ["All", "D1", "D2", "D3"])

if job_filter != "All":
    filtered_data = data[data['job_id'] == job_filter]
else:
    filtered_data = data

st.dataframe(
    filtered_data[['job_id', 'client_name', 'direction', 'scheduled_time', 'status']], 
    use_container_width=True
)

st.divider()

# 5. Support Engineering Deep Dive
st.subheader("🔧 Escalation & Error Investigation")
st.markdown("Select a failed job below to view the raw simulated output logs.")

failures = data[data['status'] == 'Failed']

if not failures.empty:
    for index, row in failures.iterrows():
        with st.expander(f"Investigate {row['job_id']} for {row['client_name']} (Scheduled: {row['scheduled_time']})"):
            st.error(f"**Error Details:**\n\n{row['error_log']}")
            st.code(f"// Raw system log snippet\n[WARN] Connection attempt to {row['client_name']} endpoint failed.\n[FATAL] {row['error_log']}\n[INFO] Retrying job in 15 minutes...")
else:
    st.success("No failed jobs to investigate right now. All systems operational.")