from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from allauth.core.exceptions import ImmediateHttpResponse
from django.contrib import messages
import logging
import os

logger = logging.getLogger(__name__)

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    
    def get_allowed_emails(self):
        """
        Get allowed emails from environment variable
        """
        allowed_emails_str = os.environ.get('ALLOWED_EMAILS', '')
        if not allowed_emails_str:
            logger.warning("ALLOWED_EMAILS environment variable is not set or empty")
            return []
        
        # Split by comma and clean up whitespace
        allowed_emails = [email.strip().lower() for email in allowed_emails_str.split(',') if email.strip()]
        logger.info(f"Loaded {len(allowed_emails)} allowed emails from environment")
        return allowed_emails

    def pre_social_login(self, request, sociallogin):
        """
        Check if the email is authorized before allowing login
        """
        try:
            # Get email from the social account data
            email = sociallogin.account.extra_data.get('email', '').lower().strip()
            
            # Log for debugging
            logger.info(f"Social login attempt for email: {email}")
            
            # Get allowed emails from environment
            allowed_emails = self.get_allowed_emails()
            
            if not allowed_emails:
                # If no allowed emails are configured, deny access
                request.session['unauthorized_email'] = email
                request.session['login_error'] = "No authorized emails configured. Please contact administrator."
                logger.error("No allowed emails configured in ALLOWED_EMAILS environment variable")
                raise ImmediateHttpResponse(redirect('unauthorized'))
            
            # Check if email is in allowed list
            if email not in allowed_emails:
                # Store unauthorized email in session for display
                request.session['unauthorized_email'] = email
                logger.warning(f"Unauthorized login attempt: {email}")
                logger.debug(f"Allowed emails: {allowed_emails}")
                
                # Add a message to display to user
                messages.error(request, f"Access denied. The email {email} is not authorized to access this application.")
                
                # Redirect to unauthorized page
                raise ImmediateHttpResponse(redirect('unauthorized'))
            
            # If we reach here, the email is authorized
            logger.info(f"Authorized login for: {email}")
            
        except ImmediateHttpResponse:
            # Re-raise ImmediateHttpResponse exceptions
            raise
        except Exception as e:
            # Log any errors that occur during the check
            logger.error(f"Error in pre_social_login: {str(e)}")
            # Store error info in session
            request.session['login_error'] = f"An error occurred during login: {str(e)}"
            raise ImmediateHttpResponse(redirect('unauthorized'))

    def save_user(self, request, sociallogin, form=None):
        """
        Override to add additional logging when user is saved
        """
        user = super().save_user(request, sociallogin, form)
        logger.info(f"Successfully saved/logged in user: {user.email}")
        return user