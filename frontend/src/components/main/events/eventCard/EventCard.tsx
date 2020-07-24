/**
 * Card with name of the event
 */

import React from "react";
import { Link } from "react-router-dom";

import IconButton from "@material-ui/core/IconButton";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import Avatar from "@material-ui/core/Avatar";
import Typography from "@material-ui/core/Typography";
import ChevronRightIcon from "@material-ui/icons/ChevronRight";

import useStyles from "./styles";
import eventImg from "./event.jpg";
import { localStorageService } from "../../../../services/storage";

interface EventCardProps {
  key: number;
  event: {
    id: number;
    paymaster: {
      id: number;
      url: string;
      username: string;
    };
    url: string;
    participants_url: string;
    bills_url: string;
    payments_url: string;
    name: string;
  };
}

/**
 * Card with event name
 */
function EventCard(props: EventCardProps) {
  const classes = useStyles();

  const handleClick = () => {
    localStorageService.setEventUrl(props.event.url);
  };

  return (
    <Card className={classes.root}>
      <CardHeader
        avatar={
          <Avatar className={classes.avatar}>{props.event.name[0]}</Avatar>
        }
        title={props.event.name}
        action={
          <IconButton aria-label="settings" onClick={handleClick}>
            <Link to={`/event/${props.event.id}`}>
              <ChevronRightIcon />
            </Link>
          </IconButton>
        }
      />
      <CardMedia
        className={classes.media}
        image={eventImg}
        title="event image"
      />
      <CardContent>
        <Typography variant="body2" color="textSecondary" component="p">
          {props.event.paymaster ? (
            <span>Paymaster: {props.event.paymaster.username}</span>
          ) : (
            <span>No Paymaster</span>
          )}
        </Typography>
      </CardContent>
    </Card>
  );
}

export default EventCard;
