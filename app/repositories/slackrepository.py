from app.services.slack.slack import Slack

class SlackRepository():
    def send_data_slack(data_error):
        ''' 
            this for hit notification slack
                :data_error class:
                :return object:
        '''
        return Slack.notification_error(data_error)
