// frontend/src/components/SchedulerControl.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Paper, Typography, FormControlLabel, Switch } from '@mui/material';

const SchedulerControl = () => {
  const [scheduler, setScheduler] = useState({ task_name: 'fetch_data', enabled: false });

  useEffect(() => {
    fetchSchedulerConfig();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const fetchSchedulerConfig = () => {
    axios.get(`/scheduler/${scheduler.task_name}/`)  // Using relative URL
      .then(response => {
        setScheduler(response.data);
      })
      .catch(error => {
        console.error("Error fetching scheduler config:", error);
      });
  };

  const toggleScheduler = () => {
    const newEnabled = !scheduler.enabled;
    axios.put(`/scheduler/${scheduler.task_name}/`, null, { // Passing null as data since we're using query params
      params: { enabled: newEnabled }
    })
      .then(response => {
        setScheduler(response.data);
      })
      .catch(error => {
        console.error("Error updating scheduler config:", error);
      });
  };

  return (
    <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
      <Typography variant="h6" gutterBottom>
        Scheduler Control
      </Typography>
      <FormControlLabel
        control={
          <Switch
            checked={scheduler.enabled}
            onChange={toggleScheduler}
            color="primary"
          />
        }
        label={scheduler.enabled ? 'Enabled' : 'Disabled'}
      />
    </Paper>
  );
};

export default SchedulerControl;
