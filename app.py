import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# Title
st.title("📊 Student Performance Dashboard")

# -----------------------
# File Upload Feature
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("students.csv")

# -----------------------
# Calculations
df["Total"] = df[["Maths", "Physics", "Chemistry", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 4

# -----------------------
# Sidebar Filter
st.sidebar.header("🔍 Filter")
selected_student = st.sidebar.selectbox("Select Student", df["Name"])

filtered_df = df[df["Name"] == selected_student]

# -----------------------
# Show Data
st.subheader("📋 Student Data")
st.dataframe(df)

# -----------------------
# Show Selected Student Info
st.subheader("👤 Selected Student Details")
st.write(filtered_df)

# -----------------------
# Bar Chart
st.subheader("📊 Average Marks")
fig1, ax1 = plt.subplots()
sns.barplot(x="Name", y="Average", data=df, ax=ax1)
st.pyplot(fig1)

# -----------------------
# Subject-wise Average
st.subheader("📈 Subject-wise Average")
subject_avg = df[["Maths", "Physics", "Chemistry", "English"]].mean()

fig2, ax2 = plt.subplots()
subject_avg.plot(kind='bar', ax=ax2)
st.pyplot(fig2)

# -----------------------
# Heatmap (NEW 🔥)
st.subheader("🔥 Heatmap of Marks")
fig4, ax4 = plt.subplots()
sns.heatmap(df.set_index("Name")[["Maths","Physics","Chemistry","English"]], annot=True, cmap="coolwarm", ax=ax4)
st.pyplot(fig4)

# -----------------------
# Grade Function
def get_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

df["Grade"] = df["Average"].apply(get_grade)

# -----------------------
# Pie Chart
st.subheader("🥧 Grade Distribution")
grade_counts = df["Grade"].value_counts()

fig3, ax3 = plt.subplots()
grade_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax3)
ax3.set_ylabel("")
st.pyplot(fig3)

# -----------------------
# Insights Section (NEW ⭐)
st.subheader("💡 Insights")

top_student = df.loc[df["Average"].idxmax()]["Name"]
weak_subject = subject_avg.idxmin()

st.write(f"🏆 Top Performer: {top_student}")
st.write(f"📉 Weak Subject: {weak_subject}")