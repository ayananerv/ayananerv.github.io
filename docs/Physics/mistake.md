# A Mistake Dealing With A Free Particle In Spherical Co-ordinates.

Consider a free particle in flat space $\mathbb{{R}}^3$. The Lagrangian $L$ is

$$L=\frac{m}{2}(\dot{x}^2+\dot{y}^2+\dot{z}^2)$$

in Cartesian coordinates and

$$L=\frac{m}{2}(\dot{r}^2+r^2\dot{\theta}^2+r^2\sin^2\theta\dot{\phi}^2)$$

in spherical coordinates.

When I try to write the E-L equations of the spherical form, I have

$$\ddot{r}=r\dot{\theta}^2+r\sin^2\theta\dot{\phi}^2$$

using

$$\frac{\partial L}{\partial r}-\frac{d}{dt}(\frac{\partial L}{\partial \dot{r}})=0$$

and

$$\frac{d}{dt}(mr^2\dot{\theta})=mr^2\dot{\phi}\sin\theta\cos\theta$$

$$\ddot{\theta}=\sin\theta\cos\theta\dot{\phi}^2$$

using

$$\frac{\partial L}{\partial \theta}-\frac{d}{dt}(\frac{\partial L}{\partial \dot{\theta}})=0$$

But on the other hand, if we use multiplication rule of derivative, we can get

$$\frac{d}{dt}(r^2\dot{\theta})=\dot{\theta}\frac{d}{dt}r^2+r^2\frac{d}{dt}\dot{\theta}=2r\dot{r}\dot{\theta}+r^2\ddot{\theta}$$

So what happened?

The mistake occurs at the formula $\ddot{\theta}=\sin\theta\cos\theta\dot{\phi}^2$, that's because I didn't consider $r$ as a variable of $t$ and just divided it. The only authentic formula is

$$\frac{d}{dt}(r^2\dot{\theta})=r^2\dot{\phi}\sin\theta\cos\theta$$