from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Define common Tailwind classes for input fields
TAILWIND_INPUT_CLASSES = (
    'w-full p-2 border border-red-400 rounded-md '  # Basic width, padding, border
    'focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 ' # Focus state styles
    'placeholder-gray-500 text-gray-800 mt-2 mb-4' # Placeholder/text styling and margin
)


class SignUpForm(UserCreationForm):
    # Custom fields are defined here with widgets and custom attributes
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs={ 
            'placeholder': 'Email Address',
            'class': TAILWIND_INPUT_CLASSES # Applying Tailwind classes
        })
    )
    
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={ 
            'placeholder': 'First Name',
            'class': TAILWIND_INPUT_CLASSES # Applying Tailwind classes
        })
    )
    
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': TAILWIND_INPUT_CLASSES # Applying Tailwind classes
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply styles and customized properties to the inherited fields
        
        # Username Field
        self.fields['username'].widget.attrs['class'] = TAILWIND_INPUT_CLASSES
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        # Password 1 Field
        self.fields['password1'].widget.attrs['class'] = TAILWIND_INPUT_CLASSES
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        # Password 2 Field (Confirm Password)
        self.fields['password2'].widget.attrs['class'] = TAILWIND_INPUT_CLASSES
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'








# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms

# class SignUpForm(UserCreationForm):
# 	email = forms.EmailField(label="", widget=forms.TextInput(attrs={ 'placeholder':'Email Address'}))
# 	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={ 'placeholder':'First Name'}))
# 	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))

# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# 	def __init__(self, *args, **kwargs):
# 		super(SignUpForm, self).__init__(*args, **kwargs)

# 		# self.fields['username'].widget.attrs['class'] = 'form-control'
# 		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
# 		self.fields['username'].label = ''
# 		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

# 		# self.fields['password1'].widget.attrs['class'] = 'form-control'
# 		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
# 		self.fields['password1'].label = ''
# 		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

# 		# self.fields['password2'].widget.attrs['class'] = 'form-control'
# 		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
# 		self.fields['password2'].label = ''
# 		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'