// frontend/src/components/FieldMappingList.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { List, ListItem, ListItemText, Paper, Typography, Divider } from '@mui/material';

const FieldMappingList = () => {
  const [mappings, setMappings] = useState([]);

  useEffect(() => {
    fetchMappings();
  }, []);

  const fetchMappings = () => {
    axios.get('http://localhost:8000/mappings')
      .then(response => {
        setMappings(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the mappings!", error);
      });
  };

  return (
    <Paper elevation={3} sx={{ p: 3 }}>
      <Typography variant="h6" gutterBottom>
        Field Mappings
      </Typography>
      <List>
        {mappings.map(mapping => (
          <React.Fragment key={mapping.id}>
            <ListItem>
              <ListItemText
                primary={`${mapping.api_field} → ${mapping.db_field}`}
              />
            </ListItem>
            <Divider component="li" />
          </React.Fragment>
        ))}
        {mappings.length === 0 && (
          <Typography variant="body2" color="text.secondary">
            No mappings available.
          </Typography>
        )}
      </List>
    </Paper>
  );
};

export default FieldMappingList;
