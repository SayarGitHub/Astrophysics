import math

import matplotlib.pyplot as plt
import pandas as pd  # pip install pandas

colnames = ["Date", "JD", "Apt_GST", "Eqn_of_Time", "Apparent_RA", "Apparent_Decli", "Distance", "Ang_diam",
            "Hell_Long", "Hell_Lat", "PA_axis"]
df = pd.read_csv("AstroA1Data.txt", names=colnames)
df.set_index("Date", inplace=True)


def RA_to_deg(appr_ra):
    temp_list = appr_ra.split()
    degrees = (int(temp_list[0]) * 15) + (int(temp_list[1]) / 4) + (float(temp_list[2]) / 240)
    return degrees


df["Apparent_RA"] = df["Apparent_RA"].apply(RA_to_deg)

X = df["Apparent_RA"]
y = df["JD"]

plt.plot(y, X)
plt.xlabel("Julian Date")
plt.ylabel("RA (in degrees)")
plt.title("RA-JD plot")
plt.savefig("RA-JD plot.png", dpi=600)
plt.savefig("RA-JD plot.pdf", dpi=600)
plt.show()

for i in df["JD"]:
    if i > 8928.5:
        new_value = df.loc[df["JD"] == i, "Apparent_RA"] + 360
        df.loc[df["JD"] == i, "Apparent_RA"] = new_value

X = df["Apparent_RA"]
y = df["JD"]

plt.plot(y, X)
plt.xlabel("Julian Date")
plt.ylabel("Smooth RA (in degrees)")
plt.title("Smooth RA-JD plot")
plt.savefig("Smooth RA-JD plot.png", dpi=600)
plt.savefig("Smooth RA-JD plot.pdf", dpi=600)
plt.show()

X = df["Apparent_RA"]
y = df["JD"]

plt.plot(y, X)
plt.xlabel("Julian Date")
plt.ylabel("Smooth RA (in degrees)")
plt.title("Mean sun vs. Sun")

end_1 = [df.iloc[0]["JD"], df.iloc[0]["Apparent_RA"]]
end_2 = [df.iloc[-1]["JD"], df.iloc[-1]["Apparent_RA"]]
x_values = [end_1[0], end_2[0]]
y_values = [end_1[1], end_2[1]]

plt.plot(x_values, y_values)
plt.legend(["Sun", "Mean Sun"])

plt.savefig("Mean Sun vs. Sun.png", dpi=600)
plt.savefig("Mean Sun vs. Sun.pdf", dpi=600)
plt.show()

m = (end_2[1] - end_1[1]) / (end_2[0] - end_1[0])
df["Mean Sun"] = m * (df["JD"] - end_1[0]) + end_1[1]


def EQT_to_deg(appr_ra):
    temp_list = appr_ra.split(":")
    degrees = (int(temp_list[0]) / 4) + (float(temp_list[1]) / 240)
    return degrees


df["Eqn_of_Time"] = df["Eqn_of_Time"].apply(EQT_to_deg)

df["diff"] = df["Mean Sun"] - df["Apparent_RA"]
X = df["Eqn_of_Time"]
y = df["diff"]

plt.plot(X, y)
plt.xlabel("Eqn of Time (in degrees)")
plt.ylabel("Difference of Mean Sun and Sun (in degrees)")
plt.title("Difference vs. Eqn of Time")
plt.savefig("Difference vs. Eqn of Time.png", dpi=600)
plt.savefig("Difference vs. Eqn of Time.pdf", dpi=600)
plt.show()


def Decli_to_deg(appr_dec):
    temp_list = appr_dec.split()
    degrees = (int(temp_list[0])) + (int(temp_list[1]) / 60) + (float(temp_list[2]) / 3600)
    return degrees


df["Apparent_Decli"] = df["Apparent_Decli"].apply(Decli_to_deg)

latitude = math.radians(22.5016)  # put own latitude inside radians function
h_list = []
for i in range(len(df)):
    test = math.tan(math.radians(df.iloc[i]["Apparent_Decli"])) * math.tan(latitude)
    h_list.append(math.degrees(math.acos(-test)))

df["h"] = h_list

X = df["JD"] - 8848.5
y = df["h"]

plt.plot(X, y)
plt.xlabel("Days from Jan 1")
plt.ylabel("Rise time (in degrees)")
plt.title("Sunrise vs Number of Days")
plt.savefig("Sunrise vs Number of Days.png", dpi=600)
plt.savefig("Sunrise vs Number of Days.pdf", dpi=600)
plt.show()

X = df["JD"] - 8848.5
y = -df["h"]

plt.plot(X, y)
plt.xlabel("Days from Jan 1")
plt.ylabel("Set time (in degrees)")
plt.title("Sunset vs Number of Days")
plt.savefig("Sunset vs Number of Days.png", dpi=600)
plt.savefig("Sunset vs Number of Days.pdf", dpi=600)
plt.show()

print(df.loc[df["h"] == max(df["h"])]["JD"])
print(df.loc[df["h"] == min(df["h"])]["JD"])
