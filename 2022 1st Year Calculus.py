#!/usr/bin/env python
# coding: utf-8

# # Import Packages 

# In[ ]:


import sympy as smp
from sympy import *


# In[ ]:


x, y = smp.symbols('x y')


# In[14]:


f = x**2 + y


# In[13]:


f


# In[18]:


f.subs(x, 4)


# In[16]:


smp.sin(x)


# In[20]:


x**(3/2)


# In[21]:


x**(smp.Rational(3/2))


# # Limits

# Question 1:

# In[22]:


smp.sin(x/2 + smp.sin(x))


# In[23]:


smp.limit(smp.sin(x/2 + smp.sin(x)), x, smp.pi)


# Question 2:

# In[24]:


2*smp.exp(1/x) / (smp.exp(1/x)+1)


# In[25]:


smp.limit(2*smp.exp(1/x) / (smp.exp(1/x)+1), x, 0, dir = '+')


# In[26]:


smp.limit(2*smp.exp(1/x) / (smp.exp(1/x)+1), x, 0, dir = '-')


# Question 3:

# In[27]:


(smp.cos(x) - 1) / x


# In[29]:


smp.limit((smp.cos(x) - 1) / x, x, smp.oo)


# # Derivatives

# Question 1:

# In[32]:


((1 + smp.sin(x)) / (1 - smp.cos(x)))**2


# In[33]:


smp.diff(((1 + smp.sin(x)) / (1 - smp.cos(x)))**2, x)


# Question 2:

# In[34]:


smp.log(x, 5)**(x/2)


# In[35]:


smp.diff(smp.log(x, 5)**(x/2), x)


# Question 3:

# In[39]:


f, g = smp.symbols('f g', cls=smp.Function)
g = g(x)
f = f(x+g)


# In[40]:


f


# In[41]:


smp.diff(f, x)


# # Basic Antiderivatives

# In[43]:


smp.csc(x)*smp.cot(x)


# In[44]:


smp.integrate(smp.csc(x)*smp.cot(x), x)


# In[45]:


4*smp.sec(3*x)*smp.tan(3*x)


# In[46]:


smp.integrate(4*smp.sec(3*x)*smp.tan(3*x), x)


# In[47]:


2/smp.sqrt(1-x**2) - 1/x**smp.Rational(1,4)


# In[48]:


smp.integrate(2/smp.sqrt(1-x**2) - 1/x**smp.Rational(1,4), x)


# # Initial Value Problem
Q1. Given dy/dx = 8x + csc^2 with y(pi/2) = -7 solve for y(x)
# In[49]:


8*x + smp.csc(x)**2


# In[57]:


integral = smp.integrate(8*x + smp.csc(x)**2, x)


# In[58]:


integral


# In[62]:


C = -integral.subs(x, smp.pi/2) - 7
y = integral + C


# In[63]:


y.subs(x, smp.pi/2)


# In[64]:


y


# # More Complicated Expressions

# In[65]:


(1+smp.sqrt(x))**smp.Rational(1,3) / smp.sqrt(x)


# In[66]:


smp.integrate((1+smp.sqrt(x))**smp.Rational(1,3) / smp.sqrt(x), x)


# In[67]:


(x*(1-x**2))**smp.Rational(1/4)


# In[73]:


smp.integrate(x*(1-x**2)**smp.Rational(1/4), x)


# In[77]:


((2*x - 1)*smp.cos((3*(2*x - 1)**2 + 6)**smp.Rational(1/2))) / (3*(2*x - 1)**2 + 6)**smp.Rational(1/2)


# In[114]:


smp.integrate(((2*x - 1)*smp.cos((3*(2*x - 1)**2 + 6)**smp.Rational(1/2))) / (3*(2*x - 1)**2 + 6)**smp.Rational(1/2), x)


# # Definite Integrals

# Question 1:

# In[79]:


smp.exp(x) / smp.sqrt(smp.exp(2*x) + 9) 


# In[82]:


smp.integrate(smp.exp(x) / smp.sqrt(smp.exp(2*x) + 9), (x, 0, smp.log(4)))


# Question 2:

# In[83]:


x**10 * smp.exp(x)


# In[84]:


t = smp.symbols('t')


# In[85]:


smp.integrate(x**10 * smp.exp(x), (x, 1, t))


# # Improper Integrals

# In[87]:


16 * smp.atan(x) / (1 + x**2)


# In[89]:


smp.integrate(16 * smp.atan(x) / (1 + x**2), (x, 0, smp.oo))


# # Sequences and Series

# Question 1: 

# In[90]:


n = smp.symbols('n')


# In[91]:


6 / 4**n


# In[92]:


smp.Sum(6 / 4**n, (n, 0, smp.oo))


# In[93]:


smp.Sum(6 / 4**n, (n, 0, smp.oo)).doit()


# Question 2: 

# In[94]:


2**(n+1) / 5**n


# In[96]:


smp.Sum(2**(n+1) / 5**n, (n, 0, smp.oo))


# In[97]:


smp.Sum(2**(n+1) / 5**n, (n, 0, smp.oo)).doit()


# Question 3: 

# In[98]:


smp.atan(n) / n**1.1


# In[104]:


smp.Sum(smp.atan(n) / n**smp.Rational(11,10), (n, 1, smp.oo))


# In[105]:


smp.Sum(smp.atan(n) / n**smp.Rational(11,10), (n, 1, smp.oo)).doit()


# .doit() does not work here and we have to use an approximation method using .n()

# In[106]:


smp.Sum(smp.atan(n) / n**smp.Rational(11,10), (n, 1, smp.oo)).doit().n()


# Question 4:

# In[108]:


(1 + cos(n)) / n


# In[109]:


smp.Sum((1 + cos(n)) / n, (n, 1, smp.oo))


# In[111]:


smp.Sum((1 + cos(n)) / n, (n, 1, smp.oo)).n()


# The above answer is wrong

# In[ ]:




