from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

kmf = KaplanMeierFitter()
kmf.fit(durations=data['days'], event_observed=data['event'])

plt.figure(figsize=(8,5))
kmf.plot()
plt.title('Kaplan-Meier Survival Curve')
plt.xlabel('Days Post-Transplant')
plt.ylabel('Survival Probability')
plt.grid(True)
plt.show()